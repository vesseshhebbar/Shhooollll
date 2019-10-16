# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:30:02 2019

@author: student
"""

def binarySearch (a, l, r, t): 

    if (r >= l): 
  
        mid = (l + r)//2
  
        if(a[mid] == t): 
            return mid         
        elif a[mid] > t: 
            return binarySearch(a, l, mid - 1, t) 
        else: 
            return binarySearch(a, mid + 1, r, t) 
  
    else: 
        return(-1)
  

a = [ 1, 2, 3, 4, 5, 6, 7, 8 ] 
t = 6
  
result = binarySearch(a, 0, len(a)-1, t) 
  
if result != -1: 
    print("Element is present at index", result+1)
else: 
    print("Element is not present in array")