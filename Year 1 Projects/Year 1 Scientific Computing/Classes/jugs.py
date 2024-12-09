# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:08:15 2021

@author: princ
"""

# pylint: disable=invalid-name, no-member, C0301, C0411, W0511

class Jug:
    ''' Class defining a jug'''

    def __init__(self, capacity):
        '''initialising function'''
        self._volume = 0
        self._temp = 0
        self._capacity = capacity


    def pour_out(self, volume, into_jug=None):
        '''finds the new volume and temperature after water is transferred to a different jug (if given)'''
        if (volume == 'all') or (volume > self._volume):   #checks that the volume pours out is greater than volume in the jug
            if not into_jug is None:                     #checks that there is an instance of jug in the into_jug parameter
                into_jug.pour_in(self._volume, self._temp) #pours all the water into the other jug
            self._volume = 0                               #resets to an empty jug
            self._temp = 0
        else:
            if not into_jug is None:
                into_jug.pour_in(volume, self._temp) #otherwise the amount of water specified is transferred
            self._volume = self._volume - volume



    def _overflow(self, volume, temp):
        '''defines the function for temperature after mixing in the event of an overflow'''
        i = (self._capacity*self._temp + temp*volume)/self._capacity*volume #lays out the integrated equation
        return i-(self._temp) #takes away the integral at volume = 0 which is just the initial temperature



    def pour_in(self, volume, temperature):
        '''increases volume of water in the jug and mixes temperatures'''
        if self._volume + volume <= self._capacity: #checks that the capacity is not yet reached
            self._temp = (temperature*volume + self._temp*self._volume)/(self._volume + volume) #works out new homogeneous temperature
            self._volume = self._volume + volume
        else:
            self._volume = self._capacity #if there is an overflow the volume is capped at the capacity of the jug
            self._temp = self._overflow(volume, temperature)


    def temperature(self):
        '''returns the temperature attribute'''
        return self._temp


    def water_volume(self):
        '''returns the volume attribute'''
        return self._volume


    def capacity(self):
        '''returns the capacity attribute'''
        return self._capacity
    