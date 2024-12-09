# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:04:14 2020

@author: princ
"""

''' Calculated simulated data and store it in a file '''

import numpy as np

def simulated_activity_and_error(t, tau1, n1, tau2, n2):
    ''' calculate simulated data with counting noise and expected experimental error

    Returns
    -------
    (activity, activity_error)

    Note
    ----
    t is assumed to have equal increments and at least two data points
    '''

    # calculate activity (decays per hour)
    a1 = n1/tau1 * np.exp(-t/tau1)
    a2 = n2/tau2 * np.exp(-t/tau2)
    activity = a1 + a2
    # integration period
    dt = t[1] - t[0]
    sim_exp_error = np.sqrt(activity*dt)/dt       # <-- noise depends on counts not count rate
    activity += sim_exp_error * np.random.randn(activity.shape[0])
    return activity, sim_exp_error


t = np.linspace(0, 10, 61)      # <-- this yields 10min intervals from 0 to 10h inclusive
# life time and starting particle number for species 1 and 2
tau1 = 1.0
tau2 = 5.0
n1 = 5e4
n2 = 1e4
activity, error  = simulated_activity_and_error(t, tau1, n1, tau2, n2)
# generate a header line for the file
headerline = f'simulated data with tau1 = {tau1}, n1 = {n1}, tau2 = {tau2}, n2 = {n2}'
filename = 'simulatedactivity.txt'
# write time and activity to file
with open(filename, 'w') as fin:
    fin.write('# ' + headerline + '\n')        # <-- '#' to indicate that this is a header line
    for k in range(t.shape[0]):
        fin.write(f'{t[k]:0.6f}\t{activity[k]:0.6f}\t{error[k]:0.6f}\n')

# alternative way of saving the data (to be read with np.loadtxt())
filename2 = 'simulatedactivity2.txt'
np.savetxt(filename2, (t, activity, error), header=headerline)      # <-- header is optional