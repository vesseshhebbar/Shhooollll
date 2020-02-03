# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:45:58 2020

@author: 1MSC20

"""

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 5005

running_sum = 0.0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # internet, UDP
sock.bind(( UDP_IP_ADDRESS, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message from ", addr, " : " , data.decode())
    if(data.decode() == "q"):
        print("Quitting...")
        break
    
    try:
        running_sum += float(data.decode())
    except:
        sock.sendto(str("e").encode(), addr)
    print("The running sum so far is ", running_sum)
    sock.sendto(str(running_sum).encode(), addr)