# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:18:15 2020

@author: 1msc20
"""

## helloworld.py
import tkinter as tk
import pygubu


class HelloWorldApp:
    
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('sad2.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')
        self.button = builder.get_object('button')
        self.textu = builder.get_object('text')
        
    def run(self):
        self.mainwindow.mainloop()
        
    def btn_clicked(self):
        val = self.textu.cget('text')
        print(val)
        self.textu.configure(textEntry='asdsad')
        

if __name__ == '__main__':
    app = HelloWorldApp()
    app.run()