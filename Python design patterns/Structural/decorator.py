# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:03:46 2024

@author: princ
"""

"""Challenge is to add new features to an existing object using
dynamic changes and not using subclassing"""

from functools import wraps

def make_blink(function):
    """Defines the decorator"""
    
    #This makes the decorator transparent in terms of its name and docs
    @wraps(function)
    
    #Define the inner function
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()
        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
        
    return decorator

#Apply decorator here!
@make_blink
def hello_world():
    """Original function! """
    
    return "Hello, World!"

#Check the result of decorating
print(hello_world())
#Check if the function name is still the same of the function being decorated
print(hello_world.__name__)
#Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)
