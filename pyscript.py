#!/usr/bin/python

import pexpect
import json
import re

### Open a file to mimic show ip BGP
F = open("output.txt", "r")
output = F.read()
print(output)
# output = "172.123.123.123"

### RegEx
RegEx = re.compile(r"> ((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))",re.M|re.I)
matchObj = RegEx.findall(output)

### Manage the json DB
print("Json Part:")
jdata = json.loads(open ('database.json').read())
# print(jdata.get("172.16.0.1","key not found"))

# loop through the objects that matches the regex, if exist increment by 1, else insert new entry
for x in matchObj:
    print(x)
    if jdata.get(x):
        jdata[x] = jdata[x] + 1
    else:
        jdata[x] = 1

print(jdata)

# write the new json to the file
with open('database.json', 'w') as outfile:
    json.dump(jdata, outfile)
