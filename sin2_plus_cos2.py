# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:10:58 2016

@author: LydiaRoth
"""

from math import sin, cos, pi 
x = pi/2

value = sin(x)**2 + cos(x)**2
print value

v0 = 3 #m/s
t = 1 # s
a = 2 #m/s**2
s = v0*t + 0.5*a*t**2
print s
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 +2*a*b + b2
eq2_sum = a2 - 2*a*b + b2 
eq1_pow = (a+b)**2
eq2_pow = (a-b)**2 
print eq1_pow, eq2_pow
print eq1_sum, eq2_sum #yeah there the same 
