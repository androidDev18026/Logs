#!/usr/bin/python3

import re
from sys import stdin as input_stream

valid_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\w{1,3}$")
valid_date = re.compile(r"\d{4}-\d{2}-\d{2}$")
valid_time = re.compile(r"\d{2}:\d{2}:\d{2}$")

for line in input_stream:
    ip, date, time = line.strip().split(',')[:3]

    # emit <ip,<date,time>> pairs 
    if valid_ip.match(ip) and valid_date.match(date) and valid_time.match(time):
        print ("%s,%s,%s" %(ip,date,time))
