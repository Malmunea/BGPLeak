#!/usr/bin/python
import subprocess

#COMMAND = "grep -E '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' ./output.txt"  

#subprocess.call(COMMAND, shell=True)

import sys
 
HOST="127.0.0.1"
ssh = subprocess.Popen(["ssh",
                        "%s" % HOST],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)
 
# send ssh commands to stdin
ssh.stdin.write("ls .\n")
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.close()
 
# fetch output
for line in ssh.stdout:
	print(line),
#subprocess.call(commands, shell=True)
