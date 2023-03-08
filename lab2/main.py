#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    num = len(format_string)
    idx = 0
    while idx < num:
        if format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+2].isdigit and format_string[idx+3] == 'k':
            length = int(format_string[idx+2])
            param = param.swapcase()
            print(param[0:int(format_string[i+2])], end="")
            idx = idx + 4
        elif format_string[idx] == '#' and format_string[idx+1] == 'k':
            print(param.swapcase(),end="")
            idx = idx + 2
        else:
            print(format_string[idx],end="")
            idx = idx + 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
