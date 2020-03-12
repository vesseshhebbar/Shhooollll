# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:06:51 2020

@author: 1msc20
"""

import tkinter as tk

class PasswordWidget(tk.Frame):
    def __init__(self, parent, label, default=""):
        tk.Frame.__init__(self, parent)
        
        self.entry = tk.Entry(self, show="*")
        
        self.entry.pack(side="bottom", fill="x", padx=4)
        
    
    
    def get(self):
        return self.entry.get()
    
if __name__ == "__main__":
    root = tk.Tk()
    PasswordWidget(root).place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()