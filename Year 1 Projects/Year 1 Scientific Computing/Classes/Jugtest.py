# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:10:24 2021

@author: princ
"""

from jugs import Jug         # <-- assumes the class Jug is defined in the file 'jugs.py'

two_litre_jug = Jug(2)
one_litre_jug = Jug(1)

two_litre_jug.pour_in(1, 15)    # <-- temperature in degrees centigrade
one_litre_jug.pour_in(1, 60)

one_litre_jug.pour_out(0.5, into_jug=two_litre_jug)
two_litre_jug.pour_out(0.5, into_jug=one_litre_jug)

print(f'The water temperature in the one litre jug is {one_litre_jug.temperature():.2f}')
print(f'The water temperature in the two litre jug is {two_litre_jug.temperature():.2f}')

two_litre_jug.pour_out('all', into_jug=one_litre_jug)

print(f'The volume of water in the one litre jug is {one_litre_jug.water_volume():.2f} litre(s)')
print(f'The volume of water in the two litre jug is {two_litre_jug.water_volume():.2f} liter(s)')

print(f'The water temperature in the one litre jug is {one_litre_jug.temperature():.2f}')
print(f'The water temperature in the two litre jug is {two_litre_jug.temperature():.2f}')