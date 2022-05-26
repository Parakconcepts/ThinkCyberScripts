#!/bin/python3

import socket
from IPy import IP



def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(' [+] Port:' + str(port) + 'is open')
	except:
		print('[-] Port' + str(port) + 'is closed')


ipaddress = input('[+] Enter Target to scan: ')		
for port in range(1,10):
	scan_port(ipaddress, port)
