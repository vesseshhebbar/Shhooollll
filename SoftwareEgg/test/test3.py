# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:18:23 2020

@author: 1msc20
"""

import encrpt as e

enc = input("Enter key:")
fil = input("Enter filename:")

e.encrypt(e.getKey(enc), fil)
e.decrypt(e.getKey(enc), "_encrypted_"+fil)