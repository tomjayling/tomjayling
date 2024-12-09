# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:00:43 2021

@author: princ
"""
#pylint: disable=invalid-name, no-member
import sympy

x, t, k_1, k_2, w, C, B = sympy.symbols('x t k_1 k_2 w C B')

#define equations for amplitudes for two stages
y_1 = sympy.cos(k_1*x-w*t) + C*sympy.cos(k_1*x+w*t)
y_2 = B*sympy.cos(k_2*x-w*t)

#find the boundary conditions at x=0 for y and y'
bc1 = (y_1 - y_2).subs(x, 0)
bc2 = (y_1.diff(x)-y_2.diff(x)).subs(x, 0)

#find the values of the constants B and C
y_sol = sympy.solve([bc1, bc2], [B, C])

#substitute in values into initial equations
y_1 = y_1.subs(y_sol)
y_2 = y_2.subs(y_sol)

#creates a compound function for amplitude either side of x=0
y_sym = sympy.Piecewise((y_1, x < 0), (y_2, x >= 0))

#turns sympy expression into numerical function
y_numpy = sympy.lambdify((x, t, k_1, k_2, w), y_sym, 'numpy')
