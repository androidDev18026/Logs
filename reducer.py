#!/usr/bin/python3

from sys import stdin as input_stream
from time import strptime

ip_, date_, hour_, mint_ = None, None, None, None
total_time = 0

for line in input_stream:

    # get < key,<value> > pairs
    ip, date, time = line.strip().split(',', 3)

    # parse ip,date,time to variables
    ip_ = ip if not ip_ else ip_
    date_, date = strptime(
        date, "%Y-%m-%d") if not date_ else date_, strptime(date, "%Y-%m-%d")
    hour, mint, _ = time.strip().split(":", 3)

    # intraday_time : minutes onsite for every distinct date (default 1)
    if ip == ip_:
        # in case hour is not initialized
        if not hour_:
            hour_, mint_, intraday_time = hour, mint, 1
        elif date == date_:
            # add 1 minute to intraday time if new entry has the same hour AND different minute
            # add 1 minute to intraday time if new entry has a different hour
            intraday_time = intraday_time + \
                1 if (hour == hour_ and mint !=
                      mint_) or hour != hour_ else intraday_time
            # update global hour_ and mint_ with the current values
            hour_, mint_ = hour, mint
        elif date > date_:
            # date changed; add previous day's time to total time for this specific ip address
            total_time += intraday_time
            # update time
            hour_, mint_, intraday_time, date_ = hour, mint, 1, date
        else:
            pass
    else:
        # new IP address
        total_time += intraday_time
        # emit output
        print("%s\t%d" % (ip_, total_time if total_time else 1))
        # reset variables after output is emitted
        ip_, hour_, mint_, total_time, intraday_time, date_ = ip, hour, mint, 0, 1, date

# handle the last input line
if ip == ip_:
    print("%s\t%d" % (ip_, total_time+intraday_time))
