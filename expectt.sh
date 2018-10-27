#!/usr/bin/expect -f

#Usage sshsudologin.expect <host> <ssh user> <ssh password> <su user> <su password>

set timeout 60

spawn ssh muneamk@localhost

expect "yes/no" { 
	send "yes\n"
	expect "*?assword" { send "12328173\n" }
	} "*?assword:" { send "12328173\n" }
expect "muneamk*"
send "ls -latr"
wait 5
close
