# -*- coding: utf-8 -*-
# pylint: disable=C0103, E0611, R0902, R0903, W0603

''' Term 2, Assignment 5

GUI part of assignment 5

Author:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from stringwave import y_numpy

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class MyMainWindow(QMainWindow):
    '"" the main window potentially with menus, statusbar, ... '""

    def __init__(self):
        super().__init__()
        self.resize(700, 300)
        self.move(400, 300)
        central_widget = MyCentralWidget(self)
        self.setCentralWidget(central_widget)
        self.setWindowTitle('PyQt widget with matplotlib animation')
        self.statusBar().showMessage('0')


class MyMplWidget(FigureCanvas):
    '"" both a QWidget and a matplotlib figure '""

    def __init__(self, main_window, figsize=(5, 3), dpi=100):
        self.main_window = main_window
        # create the figure
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # define attributes for drawing the graph
        self.frame_counter = 0
        # plot function at simulation time 0
        self.plot_y(0)
        # set up the timer for the animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timed_action)
        self.dt = 0.01 # timestep in s
        self.timer.start(self.dt*1000) # parameter is in ms
        self.start_time = time.time()

    def timed_action(self):
        ''' perform timer triggered action '''
        # record times for display
        if self.frame_counter == 0:
            self.start_time = time.time()
            t_now = self.start_time
        else:
            t_now = time.time()
        # redraw the changed elements of the figure
        self.update_y(t_now-self.start_time)
        # every time it crosses a full second, show frame time and actual time passed
        if np.floor(self.frame_counter * self.dt) != np.floor((self.frame_counter-1) * self.dt):
            mes = f'animation time = {self.frame_counter*self.dt:.1f}, '
            mes += f'actual time = {t_now-self.start_time:.1f}'
            self.main_window.statusBar().showMessage(mes)
        self.frame_counter += 1

    def plot_y(self, t):
        ''' plot the function at simulation time t '''
        self.fig.clf()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.x = np.linspace(-20, 20, 301)
        # plot and save reference to the line object
        self.line, = self.ax.plot(self.x, y_numpy(self.x, t, 1.0, 2.1, 4), 'b')
        self.ax.set_ylim([-2, 2])
        self.ax.set_xlabel('x/m')
        self.ax.set_ylabel('y/m')
        self.fig.tight_layout()
        self.draw()

    def update_y(self, t):
        ''' update the plot for simulation time t '''
        self.line.set_ydata(y_numpy(self.x, t, 1.0, 2.1, 4))
        self.ax.draw_artist(self.ax.patch) # redraw the plotting area of the axis
        self.ax.draw_artist(self.line) # redraw the plot line
        self.fig.canvas.update() # update the figure
        self.fig.canvas.flush_events() # ensure all draw requests are sent out

class MyCentralWidget(QWidget):
    '"" everything in the main area of the main window '""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        # define figure canvas
        self.mpl_widget = MyMplWidget(self.main_window)
        # place the MyMplWidget into a vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_widget) # add the figure
        #use the box layout to fill the window
        self.setLayout(vbox)


app = None

def main():
    ''' main '''
    global app
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
