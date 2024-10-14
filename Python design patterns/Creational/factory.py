# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:18:31 2024

@author: princ
"""
"""
What are design patterns?  
    - well known solutions to recurring problems
    - widely accepted by the software development community

Why use them?
    - no need to reinvent the wheel
    - encourages best practises

Essential Characteristics:
    - language neatral
    - dynamic
    - incomplete to promote customisation

3 different types:
    - creational, used to build objects systematically
    - structural, used to establish relationships between software components 
    - behavioural, used for object interactions

OOP:
    - essential for design patterns
    - objects represent problem and solution domains
    - classes are templates for creating objects

Inheritance:
    - relationship between child and parent
    - child keeps attributes and methods of parent
    - adds new attributes and methods of its own
    - overrides the existing methods of its parent

Polymorphism:
    - relies on inheritance
    - parent class is a placeholder for its child classes

Pattern Context:
    - participants, the classes used
    - quality attributes, non-functional requirements
    - forces, factors or tradeoffs to be considered
    - consequences of the design pattern
    
Pattern Language:
    - name
    - context
    - problem
    - solution
    - related patterns
    

"""
"""Factory"""

class Dog:
    
    """ a simple dog class"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"
    
class Cat:
    
    """ a simple cat class"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"
    
 
def get_pet(pet="dog"):
        
        """The Factory Method"""

        pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
        return pets[pet]

d = get_pet("dog")
print(d.speak())
   
c = get_pet("cat")
print(c.speak())



