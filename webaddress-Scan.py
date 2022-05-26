#!/bin/python3
			
import socket			#imports socket library
from IPy import IP	#Imports IPy module

def check_ip(ip):		#defines function that converts web address to ip address
	try:
	   IP(ip)
	   return(ip)
	except ValueError:
	   return socket.gethostbyname(ip)

def scan_port(ipaddress, port):			#creates portscanning function with 2 parameters
	try:
		sock = socket.socket()		#Declaring variable for sockets that connects to internet
		sock.settimeout(0.6)		#sets duration for port scanning to 0.6s
		sock.connect((ipaddress, port))
		print(' [+] Port:' + str(port) + 'is open')		#prints port status for open ports
	except:
		print('[-] Port' + str(port) + 'is closed')		#prints port status for closed ports


ipaddress = input('[+] Enter Web Address to scan: ')		#Accepts Web-address as input to scan
convert_ip = check_ip(ipaddress)

for port in range(1,100):						
    scan_port(convert_ip, port)
