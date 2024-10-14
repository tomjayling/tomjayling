# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:56:17 2024

@author: princ
"""

"""Singleton is the pattern you need when you want only
one object to be created from a class"""

"""an information cache shared by multiple objects"""

class Borg:
    
    """The Borg design pattern"""
    
    _share_data = {} # Attribute dictionary
    
    def __init__(self):
        self.__dict__ = self._share_data
        
        
class Singleton(Borg):
    
    """The singleton class"""
    """by inheriting from the Borg class the singleton
    will share all the attributes"""
    
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._share_data.update(kwargs) #update the attribute dictionary by inserting a new key-value pair
    
    def __str__(self):
        return str(self._share_data) #Returns the attribute dictionary for printing
    
#create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)