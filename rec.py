#! usr/bin/env python2	
import socket
myip="192.168.1.13"
myport=9999

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((myip,myport))
print s.recvfrom(1000)
