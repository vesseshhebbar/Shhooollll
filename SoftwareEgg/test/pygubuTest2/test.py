# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:00:37 2020

@author: 1MSC20
"""

import tkinter as tk
import pygubu


class HelloWorldApp:
    
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('test2.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('Toplevel')
        
        
    def run(self):
        self.mainwindow.mainloop()
        
    def btn_clicked(self):
        self.builder = builder = pygubu.Builder()
        button = builder.get_object('Button')
        textu = builder.get_object('Username')
        val = textu.cget('text')
        print(val)
        textu.configure(textEntry='asdsad')
        

if __name__ == '__main__':
    app = HelloWorldApp()
    app.run()