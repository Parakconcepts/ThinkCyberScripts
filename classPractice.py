#!/bin/python3
			
import socket
from IPy import IP	#Imports IPy module



def scan_port(ipaddress, port):			#creates portscanning function with 2 parameters
	try:
		sock = socket.socket()		#Declaring variable for sockets that connects to internet
		sock.settimeout(0.6)		#sets duration for port scanning to 0.6s
		sock.connect((ipaddress, port))
		print(' [+] Port:' + str(port) + 'is open')		#prints port status for open ports
	except:
		print('[-] Port' + str(port) + 'is closed')		#prints port status for closed ports


ipaddress = input('[+] Enter Target to scan: ')				#Accepts Ip address as input
for port in range(1,100):						
	scan_port(ipaddress, port)
