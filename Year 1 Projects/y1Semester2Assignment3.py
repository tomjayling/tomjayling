# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, no-member, C0301, C0411, W0511, W0613

''' Semester 2, Assignment 3

Assignment Tasks: 3

Restrictions:
    Do not change anything outside TODO blocks.
    Do not add pylint directives.
    Do not import additional modules.

Guidance:
    Angles should be defined in radians.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import numpy as np
from scipy import interpolate
from scipy import integrate
import matplotlib.pyplot as plt


class pendulum:
    ''' defines a simple pendulum '''

    def __init__(self, pendulum_length, mass):
        # TODO: Assignment Task 1: write method body
        self._length = pendulum_length
        self._mass = mass
        self._g = 0
        # End of Task 1; proceed to task 2.


    def set_g(self, g):
        ''' small g to be used in calculations '''
        self._g = g


    def dydt(self, y, t):
        """ Calculate the derivatives for a pendulum

        Parameters
        ----------
        y: array-like
            vector of unknowns for the ode equation at time t

        t: float
            time t

        Returns
        -------
        ret: numpy array of float
            the derivatives of y
        """
        # TODO: Assignment Task 2: write method body
        alpha = -(self._g/self._length)*np.sin(y[0]) #formula for angular acceleration
        ret = np.array([y[1], alpha]) #array of angular velocity and angular acceleration
        return ret
        # End of Task 2; proceed to task 3.


    def period(self, maximum_amplitude):
        ''' Calculate the period of the periodic motion.

        For amplitude=0 the small amplitude analytical solution is returned.
        Otherwise the period is calculated by integrating the ODE using
        scipy.integrate.odeint() and determining the time between release at
        maximum amplitude and the first angle=0 crossing. The exact zero
        crossing is determined using scipy.interpolate.interp1d().

        In the calculation it is assumed that the period has a value between
        90% and 150% of the small amplitude period.

        Parameters
        ----------
        maximum_amplitude: float
            maximum amplitude of the periodic motion

        Returns
        -------
        p: float
            the period
        '''
        # TODO: Assignment Task 3: write method body
        T = 0 #variable that will be returned at the end
        small_T = 2*np.pi*np.sqrt(self._length/self._g) #analytical solution for small angles
        t = np.linspace(0, 1.5*small_T/4, 101) #time range accounts for 150% of analytical solution period and only looks at first quarter of cycle
        if maximum_amplitude == 0:
            T = small_T #use analytical solution for when angle is 0
        else:
            initial_cond = np.array([maximum_amplitude, 0]) #set the initial conditions of angle and angular velocity
            sol = integrate.odeint(self.dydt, initial_cond, t) #integrate the function over the set time intervals
            f = interpolate.interp1d(sol[:, 0], t, kind='linear') #reverse the input and output to get time as a function of angle as well as interpolating over values between intervals
            T = 4*f(0) #at angle = 0 t= T/4 so multiply by 4 to get T
        return T
        # End of Task 3; no further tasks.

if __name__ == '__main__':
    #some test code
    pen = pendulum(1, 1)
    pen.set_g(9.81)

    #generate data for figure
    angles = np.linspace(0, np.pi/2, 31)
    period_ode = [pen.period(a) for a in angles]

    # generate a plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(angles, period_ode, 'b', label='generated using ode')
    ax.set_title('Period of a 1m Pendulum as a Function of Amplitude')
    ax.set_xlabel('amplitude/rad')
    ax.set_ylabel('period/s')
    ax.legend(loc='upper left')
    plt.show()
