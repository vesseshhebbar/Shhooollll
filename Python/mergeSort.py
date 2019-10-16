# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:47:05 2019

@author: student
"""

a = [4,5,6,2,3,1]

def mergeSort(a):
    if(len(a)>1):
        mid = len(a)//2
    
        L = a[:mid]
        R = a[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        l = len(L)
        r = len(R)
        i = j = k = 0
        
        while(i < l and j < r):
            if(L[i] < R[j]):
                a[k] = L[i]
                i += 1
                k += 1
            else:
                a[k] = R[j]
                j += 1
                k += 1
                
        while i < l: 
            a[k] = L[i] 
            i+=1
            k+=1
              
        while j < r: 
            a[k] = R[j] 
            j+=1
            k+=1
        
    
mergeSort(a)
print(a)


























'''
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  '''
