# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:14:08 2021

@author: princ
"""

class Ball:
    ''' class describing a ball '''

    def __init__(self, colour, material='leather', radius=None):
        self.colour = colour
        self.radius = radius
        self.material = material
        self._state = 'new'

    def __call__(self):
        return 'hello'

    def __str__(self):
        return f'A {self.colour} {self.material} ball of radius {self.radius} which is {self._state}'

    def drop_it(self):
        ''' changes the state if dropped and made of glass '''
        if self.material == 'glass':
            self._state = 'broken'

    def state(self):
        ''' returns the state, such as 'new' or 'broken' '''
        return self._state

if __name__ == '__main__':       # <-- ensures this part is not run when importing Ball from file
    print(f'dictionary of entities related to class Ball:\n{Ball.__dict__}\n')
    print(f'docstring of class Ball:\n{Ball.__doc__}\n')
    print(f"module in which Ball is defined (__main__ indicates it wasn't imported):\n{Ball.__module__}\n")


    my_glass_ball = Ball('red', material='glass')
    #print(my_glass_ball.__name__)
    print(f'class of my_glass_ball:\n{my_glass_ball.__class__}\n')
    print(f'dictionary of attributes of my_glass_ball:\n{my_glass_ball.__dict__}\n')
    print(f'representation of my_glass_ball:\n{my_glass_ball.__repr__()}\n')
    print(f'string describing my_glass_ball:\n{my_glass_ball.__str__()}\n')
    print(f'docstring of my_glass_ball (returns docstring of class):\n{my_glass_ball.__doc__}\n')
    print('\nUsing the object name in a print statement prints the return value of the __str__() method')
    print(my_glass_ball)
    print(f'\nUsing the object name in an f-string identically yields:\n{my_glass_ball}')
    print(f'\nAll attributes and methods:\n{dir(my_glass_ball)}')
    non_underscore = [a for a in dir(my_glass_ball) if a[0] != '_']
    print(f'\nAll non-underscore attributes and methods:\n{non_underscore}')
    print(f'\nAll non-underscore attributes:\n{[a for a in non_underscore if a in my_glass_ball.__dict__]}')
    print(f'\nAll non-underscore methods:\n{[a for a in non_underscore if a not in my_glass_ball.__dict__]}')

    s = my_glass_ball()
    print(f'\nmy_glass_ball() returns:\n{s}\n')