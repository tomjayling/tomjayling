# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:48:07 2022

@author: princ
"""

import numpy as np
import cv2
from PIL import Image
import os
from xlwt import Workbook


def getImages(file_name):

    #read images
    cvim = cv2.imread(file_name)
    plim = Image.open(file_name).convert('L')

    #scale to fit in laptop window
    scale = 640/cvim.shape[0]   
    cvim = cv2.resize(cvim, None, fx=scale, fy=scale)
    width, height = plim.size
    width = int((640/height)*width)
    height = 640
    plim = plim.resize((width, height))

    #create edited image
    edited = cv2.cvtColor(cvim, cv2.COLOR_BGR2GRAY)
    edited = cv2.GaussianBlur(edited, (5, 5), 0)
    edited = cv2.Canny(edited, 100, 200, apertureSize=3, L2gradient =True)

    return cvim, plim, edited


def drawCircles(cvim, plim, edited, radius):

    #Hough Circles Method
    circles = cv2.HoughCircles(edited, cv2.HOUGH_GRADIENT, 0.05, radius, 50,
        param1 = 0.1, param2 = 10, minRadius=(radius-4), maxRadius=(radius+4))
    
    #get list of pixel grayscale values
    pixels = list(plim.getdata())
    
    
    count = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))[0, :]
        for circ in circles:
            
            #get x,y coords and radius of circle
            x = circ[0]
            y = circ[1]
            r = circ[2]
            
            #check if any nearby pixels aren't white
            i = -10
            white = True
            while i < 11:
                if pixels[plim.size[0]*y+x+i] < 170:
                    white = False
                i += 1
            if white:
                
                #draw circle on image
                cv2.circle(cvim, (x, y), r, (0, 255, 0), 2)
                cv2.circle(cvim, (x, y), 2, (0, 0, 255), 3)
                count += 1

        cv2.imshow('detected circles', cvim) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return count

def getTails(foldername, radius):

    #access folder
    folder = os.listdir(foldername)
    
    total = 0
    tails = []
    for file in folder:
        file = foldername + '\\' + file
        cvim, plim, edited = getImages(file)
        t = drawCircles(cvim, plim, edited, radius)
        
        #sum up total tails
        total += t
        
        #store filename and tails for that file in a list of tuples
        file = 'C:\\Users\\princ\\' + file
        tails.append((file, t))
    return total, tails

#Main Code

folder_name = '1 pound coins new'
excel_name = 'Results3.xls'

total, individual = getTails(folder_name, radius=13)#13 for £1 / 15 for 50p

#create excel workbook
wb = Workbook()
sheet1 = wb.add_sheet('results')

i = 0
for t in individual:
    #write filename and tails for that file in two columns
    sheet1.write(i, 0, t[0])
    sheet1.write(i, 1, t[1])
    i += 1

print('The number of tails was '+str(total))

#add total to excel workbook
sheet1.write(i, 0, 'total')
sheet1.write(i, 1, total)

wb.save(excel_name)
