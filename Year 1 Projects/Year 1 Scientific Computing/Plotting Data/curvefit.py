# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:45:57 2020

@author: princ
"""

import numpy as np
from scipy.optimize import curve_fit

def sample_activity_function(t, tau1, n1, tau2, n2):
    ''' calculate activity '''
    a1 = n1/tau1 * np.exp(-t/tau1)
    a2 = n2/tau2 * np.exp(-t/tau2)
    return a1 + a2


# read the simulated data from file
data = np.loadtxt('simulatedactivity.txt')
time_sim_exp_data = data[:,0]                  # <-- extract time and activity for readability
activity_sim_exp_data = data[:,1]              #     (could also use data[:, i] directly in curve_fit call below)
activity_exp_data_error = data[:,2]

# fit data
popt, pcov = curve_fit(sample_activity_function, time_sim_exp_data, activity_sim_exp_data,
                       p0=[2, 1e4, 10, 1e4], sigma=activity_exp_data_error, absolute_sigma=True)
print(popt)