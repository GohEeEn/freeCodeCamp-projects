#!/usr/bin/python3

import socket


def banner(ip, port):
    # Create a socket object
    s = socket.socket()
    s.connect((ip, int(port)))
    # Set a timeout duration and escape if no response in 5 seconds
    s.settimeout(5)
    # Output the received data
    # Remove the 'b' character, which is suppose to mean that the information received is in byte string
    print(str(s.recv(1024)).strip('b'))


def main():
    # Get IP
    ip = input("Please enter the IP address : ")

    # Get the Port Number
    port = input("Please enter the port number : ")
    banner(ip, port)


main()
