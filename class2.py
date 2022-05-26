#!/bin/python3

import socket
from IPy import IP

ipaddress = imput('[+] Enter Target to scan: ')
port = 80
try:
	sock = socket.socket()
	sock.connect((ipaddress, port))
	print(' [+] Port 80 is open')
except:
	print('[-] Port 80 is closed')
