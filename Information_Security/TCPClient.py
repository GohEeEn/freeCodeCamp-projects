#!/usr/bin/python3

# A simple TCP client written in Python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server's IP
host = socket.gethostname()
port = 444

clientsocket.connect(('192.168.1.107', port))

# The max amount of data in bytes that allows through the port per transmission
# else divided and the transmission will be controlled by using transmission protocol
message = clientsocket.recv(1024)

clientsocket.close()
print(message.decode('ascii'))
