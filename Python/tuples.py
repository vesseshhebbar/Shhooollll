# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:33:15 2019

@author: student
"""

#1. Write a python program to create tuples with 
#   5 numbers and print the first and all items

tple = (1,2,3,4,5)
print(tple[0])
print(tple)

#2. Write a python program to get the 4th element and 5th element 
#    from the end of the 
#   tuple (Tuple is student's name)

tple = ('V','E','S','S','E','S','H')
print("\n\n",tple[-4:-3])    
print(tple[-5:-4])

#3. Write a python program to convert a list into a tuple

lis = [1,2,3,4,5,6]
print("\n\n",lis)
print(type(lis))
tple = tuple(lis)
print(tple)
print(type(tple))
    
#4. Write a python program to reverse a tuple with and without using 
#   built-in function (reversed())

tpl = (1,2,3,4,5,6)
print("\n\nUsing built-in function:\n", tuple(reversed(tpl)))

lis = list(tpl)
n = len(tpl)-1
for i in range(0, n+1):
    lis[i] = tpl[n-i]
tple = tuple(lis)
print("Without using built-in function:\n", tple)
    
    
#5. Declare a variable named str and assign the 
#   statement "Python is an easy and powerful language."
#   Split var from str and find the length (use split() )

str1 = "Python is an easy and powerful language. "
tple = str1.split(" ")
print("\n\n", tple)
print(len(tple))

#6. Write a python program which contains the 
#   name of the months in tuples.
    
#   i.   Print all items in tuples.
#   ii.  Change value of one month.
#   iii. Print first six months.

months = ("Jan","Feb","Mar","Apr","May","Jun","Jul",
          "Aug","Sep","Oct","Nov","Dec")
print("\n\n", months)
monthList = list(months)
monthList[8] = "Sept"
months = tuple(monthList)
print(months)
print(months[0:6])

#7. implicit I/P = (2,4,3,5,4,6,7,8,6,1)
#   expected O/P
#   (5,4)       (2,4,3,5,4,6)       (6,7,8,6,1) 
#    (3,5,4,6)

tple = (2,4,3,5,4,6,7,8,6,1)
print("\n")
print(tple[3:5])
print(tple[0:6])
print(tple[5:])
print(tple[2:6])

#7b.('H','E','L','L','O',' ','C','U', 'T', 'N')
#   O/P
#   ('L','O','C','T')
#   ('H','O','T')
#   ('L', ' ')

tple = ('H','E','L','L','O',' ','C','U', 'T', 'N')
print("\n\n", tple[2:9:2])
print(tple[0::4])
print(tple[3:6:2])