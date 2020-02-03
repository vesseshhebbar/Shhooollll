# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
   
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = str(input("Enter a number (press q to quit):\n")).encode()
    
    sock.sendto(msg , (UDP_IP, UDP_PORT))
    
    if(msg.decode() == 'q'):
        print("Quitting...")
        break
    
    
    data, ip = sock.recvfrom(1024)
    if(data.decode() == 'e'):
        print("please enter only numbers! ")

    print(data.decode())