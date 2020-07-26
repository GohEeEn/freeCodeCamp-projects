#!/usr/bin/python3

import re
import socket

import validators


def get_open_ports(target, port_range, isVerbose=False):
    """
    A general Port Scanner written in Python

    Args:
        target (str): A string value which is either a URL or IP address
        port_range (list): A list of two numbers indicating the first and last numbers of the range of ports to check
        isVerbose (bool, optional): Boolean value to determine if the output is in VERBOSE mode. Defaults to False.

    Return:
        In default mode, A list of open ports that are detected and in numerical order.
        In verbose mode, the open ports data will be formatted into a detailed output.
        Error message will be returned instead, when exception gets caught.
    """

    # Check if target is a valid URL
    try:
        if(validators.ipv4(target)):
            ip_address = socket.gethostbyname(target)
            try:
                url = socket.gethostbyaddr(target)[0]
            except:
                url = False
        elif(validators.ipv6(target)):
            try:
                host_info = socket.gethostbyaddr(target)
                ip_address = host_info[2][0]
                url = host_info[0]
            except:
                url = False
        else:
            ip_address = socket.gethostbyname(target)
            url = target
    except:
        if(re.search("\d+\.\d+\.\d+\.\d+", target) or
           re.search("[a-fA-F0-9]+\.[a-fA-F0-9]+\.[a-fA-F0-9]+\.[a-fA-F0-9]+", target)):
            return("Error: Invalid IP address")
        else:
            return("Error: Invalid hostname")

    # Check if given port ranges is valid
    if(not isValidPortRange(port_range)):
        return("Error: Invalid Port Range given")

    open_ports = portScanning(target, port_range)

    # Check if the output is in verbose mode
    if(isVerbose):
        verbose_output = 'Open ports for '
        verbose_output += f'{url} ({ip_address})\n' if url else f'{ip_address}\n'
        verbose_output += 'PORT     SERVICE\n'
        protocolname = 'tcp'
        for port in open_ports:
            port_str = str(port).ljust(4)
            service = socket.getservbyport(port, protocolname)
            verbose_output += (f'{port_str}     {service}')
            if port != open_ports[-1]:
                verbose_output += '\n'
        return(verbose_output)
    else:
        return(open_ports)


def isValidPortRange(port_range):
    """
    Function to validate if the given port range is valid

    Args:
        port_range (list): A list which is suppose to contain 2 integers, which is the starting and the ending port number to scan

    Returns:
        bool: Return True if the defined rules for the port range list passed, else False
    """

    if(int((port_range[0]) > int(port_range[-1])) or (len(port_range) != 2)):
        return False
    return True


def portScanning(host, port_range):
    """
    Port scanning function to scan a specific port on given host

    Args:
        host (str): A valid URL which is the scanning target
        port_range (list): A valid list of two numbers indicating the first and last numbers of the range of ports to check

    Return:
        open_ports (list): A list of open ports that are detected and in numerical order
    """

    open_ports = []
    socket.setdefaulttimeout(2)

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if(sock.connect_ex((host, port)) == 0):
            open_ports.append(port)
        sock.close()

    return(open_ports)
