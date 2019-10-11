# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:20:15 2019

@author: student
"""

# Create a list of airports that includes a series of tuples containing an airport's name and it's code.

OHare = ("O'Hare International Airport", "ORD")
LA = ("Los Angeles International Airport", "LAX")
Dallas = ("Dallas/Fortworth International Airport", "DFW")
Denver = ("Denver International Airport", "DEN")

Airports = [OHare, LA, Dallas, Denver]

for (ap, code) in Airports:
    print("The code for ", ap, " is ",code)