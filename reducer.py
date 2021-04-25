#!/usr/bin/python3

import sys
from operator import itemgetter
from itertools import groupby


def read_input():
    for line in sys.stdin:
        ip, date = line.strip().split(',',1)
        yield ip, date


for ip,date in groupby(read_input(), itemgetter(0)):
    print("%s\t%s" %(ip,len(set(map(itemgetter(1), date)))))
    
