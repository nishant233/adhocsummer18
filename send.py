#! usr/bin/env python2

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=raw_input("Enter your message :")
s.sendto(msg,("127.0.0.1",9999))
