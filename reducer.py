#!/usr/bin/python3

from sys import stdin as input_stream
from datetime import timedelta
from math import ceil

ip_,time_start,time_end=None,timedelta.min,timedelta.max
time_elapsed = timedelta.min

for line in input_stream:
    ip, time = line.strip().split(',',2)
    
    ip_ = ip if not ip_ else ip_
    hour, mint, secs = tuple(map(int,time.strip().split(":",3)))
    
    if ip == ip_ and time_start == timedelta.min:
        time_start = timedelta(hours=hour,minutes=mint,seconds=secs)
    elif ip == ip_:
        time_end = timedelta(hours=hour,minutes=mint,seconds=secs)
    else:
        if ip != ip_:
            # Calculate time elapsed for User w/ this IP address
            time_elapsed = (time_end - time_start).total_seconds()
            time_elapsed = ceil(time_elapsed / 60) if time_elapsed > 0 else 1
            # Write result to stdout
            print("%s\t%d" %(ip_, time_elapsed))
            ip_,time_start = ip,timedelta(hours=hour,minutes=mint,seconds=secs)
            time_end = timedelta(hours=hour,minutes=mint,seconds=secs)
        else:
            pass        
        
if ip == ip_:
    time_end = timedelta(hours=hour,minutes=mint,seconds=secs)
    time_elapsed = (time_end - time_start).total_seconds()
    time_elapsed = ceil(time_elapsed / 60) if time_elapsed > 0 else 1
    print("%s\t%d" %(ip_, time_elapsed))
    
    