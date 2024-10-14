# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:38:14 2024

@author: princ
"""

""" Abstract Family builds on the factory method and 
is useful when the user expectation yields multiple
related objects"""

class Dog:
    
    """ a simple dog class"""
    
    def __str__(self):
        return "Dog"
    
    def speak(self):
        return "Woof!"

class DogFactory:
    """Concrete Factory"""
    
    def get_pet(self):
        """Returns a Dog object"""
        return Dog()
        
    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"
    
class PetStore:
    """PetStore houses our Abstract Factory"""
    
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        
        self._pet_factory = pet_factory
        
    def show_pet(self):
        """Utility method to show details of the objects
        returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))
        


#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract factory
shop = PetStore(factory)

#Invoke the utility method to show details of our pet
shop.show_pet()
        