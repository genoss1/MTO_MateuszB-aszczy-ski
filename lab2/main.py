#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    num = len(format_string)
    idx = 0
    while idx < num:
        if format_string[idx] == '#' and format_string[idx+1] == 'k':
            print(param,end="")
        else:
            print(format_string[idx],end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
