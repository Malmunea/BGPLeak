#!/usr/bin/python

import pexpect
import sys
import re

### Open a file to mimic show ip BGP
F = open("output.txt", "r")
output = F.read()
print(output)
# output = "172.123.123.123"

### RegEx
RegEx = re.compile(r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",re.M|re.I)
matchObj = RegEx.findall(output)

# print(matchObj.group())
for x in matchObj:
    print(x)
