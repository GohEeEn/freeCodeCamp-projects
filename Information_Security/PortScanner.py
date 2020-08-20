#!/usr/bin/python3

# A simple, hardcoded port scanner written in Python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP you want to scan\t: ")
port = int(input("Enter the port you want to scan\t: "))


def portScanner(port):
    # Return an error code if there is a connection error or no host is found
    error_code = s.connect_ex((host, port))
    if error_code:
        print("The port " + str(port) + " is closed")
    else:
        print("The port " + str(port) + " is open")


portScanner(port)
