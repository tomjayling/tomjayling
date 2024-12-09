# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:30:58 2021

@author: princ
"""

"""import numpy as np

def polynomial(x):
    ''' fourth order polynomial'''
    return np.pi*(x**4 + 3*x**2 - 2.5*x + 0.05)

def simple_integrate(f, x_start, x_end, dx):
    ''' integrate the function f(x) from x_start to x_end '''
    x = np.arange(x_start, x_end, dx)
    y = f(x + dx/2)    # uses value at mid point
    return y.sum()*dx
    
def simpsons_integrate(f, x_start, x_end, dx):
    ''' integrate the function f(x) from x_start to x_end using the Simpson's rule'''
    x = np.arange(x_start, x_end, dx)
    y = 1/6 * (f(x) + 4*f(x+dx/2) + f(x+dx))    # uses parabolic approximation
    return y.sum()*dx 

for n in [2, 3, 4, 5, 100, 1000, 1001, 10000, 10001]:
    xs = 0
    xe = 1
    dx = (xe-xs)/(n-1)
    si = simple_integrate(polynomial, xs, xe, dx)
    spi = simpsons_integrate(polynomial, xs, xe, dx)
    print(f'simplistic integration using {n} values yields {si:e}')
    print(f"Simpson's integration using {n} values yields {spi:e}")
    print('')

print('Note: The analytically derived exact result is 0')
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

temperature = np.linspace(200, 320, 7)
c = np.array([10.1, 10.2, 10.8, 11.6, 12.6, 14.0, 16.2])       # <-- (not the values for water)

c_nearest = interp1d(temperature, c, kind='nearest')

c_linear = interp1d(temperature, c, kind='linear')

c_quadratic = interp1d(temperature, c, kind='quadratic')


t_val = 297
c_val = c_nearest(t_val)
print(f'Nearest value for T = {t_val} K: c = {c_val}')

c_val = c_linear(t_val)
print(f'Linearly interpolated value for T = {t_val} K: c = {c_val}')

t_val = 290
c_val = c_quadratic(t_val)
print(f'Quadratically interpolated value for T = {t_val} K: c = {c_val}')

x = np.linspace(200, 320, 101)
yl = c_linear(x)
yq = c_quadratic(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(temperature, c, 'bo', label='tabulated samples')
ax.plot(x, yl, 'g-', label='linear interpolation')
ax.plot(x, yq, 'r-', label='quadratic interpolation')
ax.legend(loc='upper left')
plt.show()