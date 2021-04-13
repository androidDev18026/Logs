#!/usr/bin/python3

import sys

for line in sys.stdin:
    ip, date, time = line.strip().split(',')[:3]
    
    if ip[0].isdigit():
        print ("%s,%s" %(ip, ''.join(date[-2:]+time[:5].replace(':',''))))