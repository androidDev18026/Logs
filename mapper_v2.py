#!/usr/bin/python3

import sys

minute_ips = set()

def valid(ip):
    return ip[0].isdigit()

def distinct(ip, p_date ,date ,p_time ,time):
    global minute_ips
    
    if date == p_date and time[:5] == p_time[:5]:
        if ip in minute_ips:
            return False 
    else:
        minute_ips.clear()
        
    minute_ips.add(ip)
    
    return True 
    
   
p_date, p_time = None, None

for line in sys.stdin:
    
    ip, date, time = line.strip().split(',')[:3]
    
    p_date = date if not p_date else p_date
    p_time = time if not p_time else p_time
        
    if valid(ip) and distinct(ip,p_date,date,p_time,time):
        print("%s,%s" %(ip,''.join(date.replace('-','')+time[:5].replace(':','')))) 
        p_date, p_time = date, time
    