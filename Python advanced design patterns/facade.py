# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:10:46 2024

@author: princ
"""

"""Design patterns are low level and concrete whereas architechtural
patterns are high-level and abstract"""

"""The impact of a design pattern is local whereas architechtural patterns
have a direct impact on the whole software"""

"""Procedural programming: using functions. Object-orientated
programming: using properties and behaviours."""

"""Python is an object-orientated language and design patterns
require the use of OOP."""

"""Domain examples: Real-Time (RT), Human-computer interface (HCI),
 J2EE, Security"""
 
"""Facade is useful when you want to reduce complexity and protect 
client classes in the subsystem"""
 
class SubsystemA:

    def method1(self):
        print('SubsystemA method1 ...')
        
    def method2(self):
        print('SubsystemA method2 ...')

class SubsystemB:
    
    def method1(self):
        print('SubsystemB method1 ...')
        
    def method2(self):
        print('SubsystemB method2 ...')

class Facade:

    def __init__(self):
        self._subsystem_A = SubsystemA()
        self._subsystem_B = SubsystemB()

    def method(self):
        self._subsystem_A.method1()
        self._subsystem_A.method2()
        self._subsystem_B.method1()
        self._subsystem_B.method2()

def main():
    facade = Facade()
    facade.method()

if __name__ == "__main__":
    main()
