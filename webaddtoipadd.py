#!/bin/python3
import socket
from IPy import IP



def check_ip(ip):		#defines function that converts web address to ip address
	try:
	   IP(ip)
	   return(ip)
	except ValueError:
	   return socket.gethostbyname(ip)
	  
webadd= input('input webadd: ')
res_webadd = check_ip(webadd)
print(res_webadd)
