# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:27:28 2020

@author: 1msc20
"""

import tkinter as tk

r = tk.Tk() 
r.title("Password Manager Home Page")

r.geometry("300x100") 

button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 

