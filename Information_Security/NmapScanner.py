#!/usr/bin/python3

# A simple Nmap port scanner written in Python

import nmap

# Create a Nmap port scanner object
scanner = nmap.PortScanner()

print("\nWelcome, this is a simple nmap automation tool")
print("---------------------------------------------------------")

ip_addr = input("Enter the IP address to scan : ")
print("The IP you entered is : ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run :
1) SYK ACK Scan
2) UDP Scan
3) Comprehensive Scan
""")

print("You have selected option : ", resp)

nmap_version_tuple = scanner.nmap_version()
nmap_version_str = '.'.join(map(str, nmap_version_tuple))
print("Nmap Version @", nmap_version_str)

if resp == '1':
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())

    # If the IP address service is up/down
    print("IP Status : ", scanner[ip_addr].state())

    # Display which protocol we are scanning for
    print(scanner[ip_addr].all_protocols())

    # Return all reachable ports within the specified range
    print("Open Ports : ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status : ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports : ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status : ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports : ", scanner[ip_addr]['tcp'].keys())

else:
    print("Please enter a valid option")
