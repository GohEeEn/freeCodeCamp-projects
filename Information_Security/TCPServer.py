#!/usr/bin/python3

# A simple TCP server implemented in Python3

import socket

# Create a socket object with :
#
# AF_INET       = IPv4, an address family that is used to designate
#                 the type of addresses that your socket can communicate with
#                 (Socket Family)
# SOCK_STREAM   = TCP socket, a connection-based protocol, which is established
#                 and the two parties have a conversation until the connection
#                 is terminated by one of the parties or by a network error
#                 (Socket Type)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host's name
# host = '192.168.1.107'
host = socket.gethostname()
port = 444

# Binding to socket
# host will be replaced with IP, if changed and not running on host
serversocket.bind((host, port))

# TCP listener, specify the max number of tcp clients it can receive
serversocket.listen(3)

while True:
    # Accept the TCP connection from the client
    clientsocket, address = serversocket.accept()
    print("Received connection from " % str(address))
    message = 'Hi ! Thank you for connecting to the server' + "\r\n"

    # Message sent to client to notify they have successfully connect to the server
    clientsocket.send(message.encode('ascii'))

    # Close the current TCP connection
    clientsocket.close()
