# -*- coding: utf-8 -*-

import socket
   
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = str(input("Enter a URL: (press q to quit)\n")).encode()
    
    sock.sendto(msg, (UDP_IP, UDP_PORT))
    
    if(msg.decode() == 'q'):
        break
    # output the response (if any)
    data, ip = sock.recvfrom(1024)

    print(data.decode())