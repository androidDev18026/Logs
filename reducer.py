#!/usr/bin/python3

import itertools
import operator
import sys


def read_input():
    for line in sys.stdin:
        ip, date = line.strip().split(',',1)
        yield ip, date


for group in itertools.groupby(read_input(), operator.itemgetter(0)):
    print("%s\t%s" %(group[0],len(set(map(operator.itemgetter(1), group[1])))))

