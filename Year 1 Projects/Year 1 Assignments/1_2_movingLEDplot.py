# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:52:42 2020

@author: princ
"""

''' Plot activity of a radioactive sample with two independent species '''
# -*- coding: utf-8 -*-
# pylint: disable=E0012, R0913, C0413, C0411, invalid-name, no-member, C0301, W0622

''' Assignment 2 (plotting; compulsory)

Assignment Tasks: 2

Aim:
    Plot the trace of a flashing LED mounted on a moving rotating disk.
    (Think of a long shutter time photo exposure.)

Restrictions:
    Do not change anything outside TODO blocks.
    Do not use import, for or other loops.
    Do not add pylint directives.
    Do not use scatter(), use plot().

Guidance:
    Everything is in SI units.
    You can change the 'plot_it' flag starting out on line 155 to switch
    between displaying the plot and running the unit tests.

    The process of writing a program with several functions can be approached
    in a number of different ways:

    1. Write everything, then test as a whole. This is ambitious.
    2. Write pass-through/dummy versions of all functions first to ensure
       there is some output to monitor, then flesh out the functions
        incrementally.
    3. Step through the code line-by-line using F9 to execute individual lines.

    For this assignment I would recommend approach 2. You would first update
    'generate_plot' to draw a simple unlabelled plot of the (x,y) positions.
    Then you can work on 'LED_position()' and monitor progress by looking
    at the plot.

    Task 1:
        Make sure the time array exhibits the correct duration.

    Task 2:
        Generate a fully labelled graph, giving units where appropriate.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import numpy as np
import matplotlib.pyplot as plt

def LED_position(centre_height, disk_radius, centre_velocity,
                 angular_velocity, time_increment, duration):
    """ Calculate the location of an LED on a moving rotating disk

    Consider a rotating disk with a LED at attached at its edge. The disk is
    moved along x (the horizontal) with its rotational axis held perpendicular
    to x and the vertical y. The function calculates the location of the LED
    in the fixed observer frame as a function of time.

    At time zero the centre of the disk is at x = 0 and the LED is at
    x = - disk_radius.

    The sense of rotation is such that dy/dt < 0 at t = 0.

    All quantities are in SI units.

    Parameters
    ----------
    centre_height: float
        height of the centre of the disk.

    disk_radius: float
        radius of the disk

    centre_velocity: float
        velocity of the disks' centre along x.

    angular_velocity: float
        angular velocity of the disk

    time_increment: float
        dt for calculation

    duration: float
        time period of calculated motion

    Returns
    -------
    (t, x, y) : arrays of floats
        arrays giving time, and corresponding x, and y position of the LED
    """

    # TODO: Assignment Task 1: write function body  # pylint: disable=fixme
    t = np.linspace(0, duration, int(duration/time_increment)+1) # generates an array of time intervals to take measurements at
    x = (centre_velocity)*t - disk_radius*np.cos(angular_velocity*t) #works out the x coordinate for each time interval in t
    y = centre_height - disk_radius*np.sin(angular_velocity*t) #works out the y coordinate for each time interval in t
    return (t, x, y)
    # End of Task 1; proceed to Task 2


def generate_plot(ax, t, x, y, time_steps_per_flash):
    """ Creates a fully labelled (parametric) plot of the LED position

    (x(t),y(t)) pairs are plotted as a blue line.
    Assumes the LED is flashing with a constant frequency and is on at t=0.
    Draws red markers at the locations of these LED flashes.

    Uses y=0 as the lower limit for the y axis.
    Provides an annotation text identifying the flashing frequency, as in
    'Flashing frequency = 10 Hz'.
    Provides an annotation text with your name and date (the date is that of
    writing the program, not date of running the program).
    Provides a title of the plot 'LED on moving rotating disk'.
    Displays a legend.

    Do not use scatter(), use plot().

    Parameters
    ----------

    ax: matplotlib axes
        object to draw the graph into

    t, x, y: arrays of floats
        time and corresponding x and y values.

    time_steps_per_flash: integer
        time steps (in array t) per flash cycle

    Returns
    -------
    ax: matplotlib axes
        fully labelled plot
    """
    # TODO: Assignment Task 2: write function body # pylint: disable=fixme    
    #figure showing horizontal and vertical displacement
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    #plot the x and y values in blue
    ax.plot(x, y, 'b', label='Path of the LED')
    #plot the x and y values when the LED flashes with red crosses (indicating frequency)
    ax.plot(x[::time_steps_per_flash], y[::time_steps_per_flash], 'r+', label='Frequency')
    ax.set_ylim(0, 2)
    #write labels and text for name and graph title
    ax.set_ylabel("vertical displacement")
    ax.set_xlabel("horizontal displacement")
    ax.legend()
    ax.text(0.98, 0.02, 'Thomas Ayling\n17.11.2020', transform=ax.transAxes,
            horizontalalignment='right', fontsize=14)
    ax.text(0.7, 0.9, 'Path of an LED attatched to a moving disk', transform=ax.transAxes,
            horizontalalignment='right', fontsize=14)
    ax.text(0.98, 0.8, 'Frequency = 10Hz', transform=ax.transAxes,
            horizontalalignment='right', fontsize=14)
    plt.show()
    # End of Task 2;  no further tasks.


def flash_and_plot():
    ''' calculates the motion of a LED and generates a plot '''
    centre_height = 1
    disk_radius = 0.5
    centre_velocity = 1
    angular_velocity = 3
    duration = 7
    time_increment = 0.01
    time_steps_per_flash = 4
    t, x, y = LED_position(centre_height, disk_radius, centre_velocity,
                           angular_velocity, time_increment, duration)
    fig = plt.figure(num=1, figsize=(16, 12))
    ax = fig.add_subplot(1, 1, 1)
    generate_plot(ax, t, x, y, time_steps_per_flash)
    plt.show()



if __name__ == '__main__':
    # pylint: disable=E0012, C0112, C0111, C0304, C0325, C0413, C0411, C0301
    # Feel free to modify this flag to switch between plotting and unit tests
    plot_it = True
    if plot_it:
        # plot a test figure
        flash_and_plot()
    else:
        # do the unit tests
        import unittest

        class LED_positionTests(unittest.TestCase):
            ''' tests LED_position '''

            def test_points(self):
                ''' tests correct number of points '''
                self.assertEqual(LED_position(0, 0, 1, 10, 1, 1)[0].shape, (2,))

            def test_start_time(self):
                ''' tests correct start time '''
                self.assertEqual(LED_position(0, 0, 1, 10, 0.1, 1)[0][0], 0)

            def test_end_time(self):
                ''' tests correct end time '''
                self.assertEqual(LED_position(0, 0, 1, 10, 0.1, 1)[0][-1], 1)

            def test_xstart(self):
                ''' tests correct x start position '''
                self.assertEqual(LED_position(5, 1, 1, 10, 0.1, 1)[1][0], -1)

            def test_ystart(self):
                ''' tests correct y start position '''
                self.assertEqual(LED_position(5, 1, 1, 10, 0.1, 1)[2][0], 5)

            def test_rotation(self):
                ''' tests sense of rotation '''
                self.assertLess(LED_position(0, 1, 1, 10, 0.1, 1)[2][1], 0)


        unittest.main(exit=False)