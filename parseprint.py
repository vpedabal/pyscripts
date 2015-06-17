#!/usr/bin/python
import string
import sys
print "Hello, world"

f = open('print.txt', 'r')
print f
str = f.readline()
str = f.readline()
splitstr = string.split(str,',')
for i in splitstr:
    splititem = string.split(i,'=')
    sys.stdout.write(splititem[0] + ',')
print ""

while str != "":
    str = f.readline()
    str = f.readline()
    splitstr = string.split(str,',')
#    print splitstr
    for i in splitstr:
        splititem = string.split(i,'=')
        splitvalue = string.split(splititem[1],':')
        sys.stdout.write(splitvalue[0] + ',')
#        sys.stdout.write(splititem[1] + ',')
    print ""


