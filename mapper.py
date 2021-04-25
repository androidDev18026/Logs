#!/usr/bin/python3

import sys
import re

valid_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\w{1,3}$")

for line in sys.stdin:
    ip, date, time = line.strip().split(',')[:3]
    
    if valid_ip.match(ip):
        print ("%s,%s" %(ip, ''.join(date.replace('-','')+time[:5].replace(':',''))))
        
