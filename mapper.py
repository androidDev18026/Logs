#!/usr/bin/python3

import re
from sys import stdin as input_stream
from time import strptime

valid_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\w{1,3}$")
valid_date = re.compile(r"\d{4}-\d{2}-\d{2}$")
valid_time = re.compile(r"\d{2}:\d{2}:\d{2}$")

def valid_input(ip, date, time):
    return True if valid_ip.match(ip) and valid_date.match(date) and valid_time.match(time) else False

def redundancy_check(c_ip,p_ip,c_d,p_d,c_t,p_t):
    if c_ip==p_ip and strptime(c_d, "%Y-%m-%d")==strptime(p_d, "%Y-%m-%d"):
        return True if c_t.strip().split(":")[1] != p_t.strip().split(":")[1] else False 
    else:
        return True
    
    
prev_ip, prev_date, prev_time = None,None,None

for line in input_stream:
    
    curr_ip, curr_date, curr_time = line.strip().split(',')[:3]
    
    prev_ip = curr_ip if not prev_ip else prev_ip
    prev_date = curr_date if not prev_date else prev_date
    prev_time = curr_time if not prev_time else prev_time
    
    # emit <ip,<date,time>> pairs 
    if valid_input(curr_ip,curr_date,curr_time):
        if redundancy_check(curr_ip,prev_ip,curr_date,prev_date,curr_time,prev_time):
            print ("%s,%s,%s" %(curr_ip,curr_date,curr_time))
        prev_ip,prev_date,prev_time=curr_ip,curr_date,curr_time
    else:
        pass
        
