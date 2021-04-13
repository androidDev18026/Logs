#!/usr/bin/python3

import sys

ip_,date_ = None,None
total = [1]

for line in sys.stdin:
        
    ip, date = line.strip().split(',',1)
   
    ip_ = ip if not ip_ else ip_
    date_ = date if not date_ else date_
        
    if ip == ip_:
        if date != date_:
            total.append(1)
            date_ = date
        else:
            continue
    else:
        print ("%s\t%s" %(ip_,str(sum(total))))
        ip_,date_ = ip, date
        total = [1]
    
if ip == ip_:
    print ("%s\t%s" %(ip_,str(sum(total))))
        
