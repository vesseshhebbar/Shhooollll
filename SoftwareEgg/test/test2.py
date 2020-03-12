# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:43:27 2020

@author: 1msc20
"""

import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

print("Opened database successfully")

cur.execute("SELECT * FROM COMPANY")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
print("Records created successfully")
conn.close()