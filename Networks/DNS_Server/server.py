# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:45:58 2020

@author: 1MSC20

"""

import socket
from urllib.parse import urlparse

import lookup
mydict = lookup.mydict

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # internet, UDP
sock.bind(( UDP_IP_ADDRESS, UDP_PORT))

dict = eval(open("lookup.txt").read())

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode()
    print("received URL: ", data)
    if(data == "q"):
        break
    
    if (("http://" not in data) and ("https://" not in data)):
        data = "http://" + data
        
    data = urlparse(data).netloc
    
    if ("www." in data):
        data = data.replace("www.", "")

    
    ip = "Error 404: requested location not present in lookup table! "
        
    try:
        ip = mydict[data]
    except:
        print("Error 404")

    print("matching IP address: ", ip, '\n')
    sock.sendto(ip.encode(), addr)
    
