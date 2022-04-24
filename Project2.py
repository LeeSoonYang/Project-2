# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:12:46 2020

@author: keroy
"""


import math


def newton(x):
    x1 = x-((3*math.sin(math.radians((x**2)/3)))\
            /(2*x*math.cos(math.radians((x**2)/3))))
    if x1 == 0:
        return x
    elif x-x1 < 0.000001:
        return x
    else:
        x = x1
        return newton(x)
      
while True:
    try:
        x = input("Please enter an number:")  
        if x == '0':
            print('Please enter a non-zero number')
        elif type(float(x)) == float:
            print(newton(float(x)))
    except:
        print('Input is not a number')
        

    
    