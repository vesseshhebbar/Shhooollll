
import socket
   
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = str(input("Enter a message: ")).encode()
    sock.sendto(msg , (UDP_IP, UDP_PORT))
