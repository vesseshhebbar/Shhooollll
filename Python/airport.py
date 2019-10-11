# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:42:42 2019

@author: student
"""

OHare=("O'Hare International Airport","ORD")
LA=("Los Angels International Airport","LAX")
DF=("Dallas/Fort Worth International Airport","DFW")
D=("Denver International Airport","DEN")
Airports=[OHare,LA,DF,D]
for (airport,code) in Airports:
    print("The code for",airport,"is",code)