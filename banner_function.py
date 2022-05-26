#!/bin/python3
			#Scripts for Mutiple targets or Web urls
import socket			#imports socket library
from IPy import IP	#Imports IPy module

def scan(targets):
	convert_ip = check_ip(targets)
	print('\n' + '[ Scanning Target] ' + str(targets))
	for port in range(1,100):						
    		scan_port(convert_ip, port)


def check_ip(ip):		#defines function that converts web address to ip address
	try:
	   IP(ip)
	   return(ip)
	except ValueError:
	   return socket.gethostbyname(ip)
	   
def get_banner(s):
	return s.recv(1024)	  

def scan_port(ipaddress, port):			#creates portscanning function with 2 parameters
	try:
		sock = socket.socket()		#Declaring variable for sockets that connects to internet
		sock.settimeout(0.6)		#sets duration for port scanning to 0.6s
		sock.connect((ipaddress, port))
		try:
			banner = get_banner(sock)
			print('[+] Open port' + str(port) + ':' + str(banner.decode().strip('\n')))
		except:
			print(' [+] Open port' + str(port))
	except:
		pass	
		
targets= input('[+] Enter Multiple Targets/Web Address(es) to scan(split multiple targets): ')		#Accepts Multiple Web-address as input to scan
if ',' in targets:
	for ip_add in targets.split(','):
		scan(ip_add.strip(' '))
else:
    scan(targets)		




	
	
	
	
	
