#!/usr/bin/python3

from sys import stdin as input_stream
from datetime import timedelta
from time import strptime
from math import ceil

ip_,time_start,time_end=None,timedelta.min,timedelta.max
time_elapsed = timedelta.min
date_ = None
total_time_elapsed,intraday_time_elapsed = 0,0

for line in input_stream:
    
    # get key <value> pairs (3) 
    ip, date, time = line.strip().split(',',3)
    
    # parse ip,date,time to variables
    ip_ = ip if not ip_ else ip_
    date_,date = strptime(date, "%Y-%m-%d") if not date_ else date_,strptime(date, "%Y-%m-%d")
    hour, mint, secs = tuple(map(int,time.strip().split(":",3)))
    
    # handle first line of input by initializing start time
    if ip == ip_ and time_start == timedelta.min:
        time_start = timedelta(hours=hour,minutes=mint,seconds=secs)
    
    # if the address is the same & the date is the same assign time_end to
    # current time in case there is no other entry for that day  
    elif ip == ip_ and date == date_:
        time_end = timedelta(hours=hour,minutes=mint,seconds=secs)
    
    # if the address is the same but we are not on the same day add the intraday
    # time to the total time and set the current date to the date from the input 
    elif ip == ip_ and date > date_:
        intraday_time_elapsed = (time_end - time_start).total_seconds()
        total_time_elapsed += intraday_time_elapsed if intraday_time_elapsed > 60 else 60
        time_start = timedelta(hours=hour,minutes=mint,seconds=secs)
        time_end = timedelta(hours=hour,minutes=mint,seconds=secs) 
        date_ = date
    else:
        # found new IP address 
        if ip != ip_:
            # calculate time elapsed for this IP address
            intraday_time_elapsed = (time_end - time_start).total_seconds()
            total_time_elapsed += intraday_time_elapsed if intraday_time_elapsed > 60 else 60
            total_time_elapsed = ceil(total_time_elapsed / 60) if total_time_elapsed > 0 else 1
            # write result to stdout
            print("%s\t%d" %(ip_, total_time_elapsed))
            # reset variables after output is emitted
            ip_,time_start = ip,timedelta(hours=hour,minutes=mint,seconds=secs)
            time_end, date_ = timedelta(hours=hour,minutes=mint,seconds=secs),date
            total_time_elapsed = 0
        else:
            pass        

# handle the last input line
if ip == ip_:
    time_end = timedelta(hours=hour,minutes=mint,seconds=secs)
    intraday_time_elapsed = (time_end - time_start).total_seconds()
    total_time_elapsed += intraday_time_elapsed if intraday_time_elapsed > 60 else 60
    total_time_elapsed = ceil(total_time_elapsed / 60) if total_time_elapsed > 0 else 1
    print("%s\t%d" %(ip_, total_time_elapsed))