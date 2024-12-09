# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:48:54 2021

@author: princ
"""

import numpy as np
import matplotlib.pyplot as plt 

def pdf(x):
    ''' range -1 to 1 '''
    return 1.5 * x**2

def cdf(x):
    ''' range -1 to 1 '''
    return 0.5*(x**3 + 1)

def inv_cdf(y):
    ''' input range 0 to 1 '''
    x3 = 2*y - 1
    return np.power(np.abs(x3), 1/3)*np.sign(x3)

def rv(n):
    ''' random variable with PDF giving rise to inv_cdf() '''
    x = np.random.rand(n)
    return inv_cdf(x)

x_rand = rv(1000)                   # <-- draw 1000 random values
y_arr = np.zeros(x_rand.shape)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x_rand, y_arr, '.')
ax.set_xlabel('x position')
ax.set_ylabel('y position')
ax.set_title('Random distribution of points along x with $PDF(x) = (3/2) x^2$')
plt.show()