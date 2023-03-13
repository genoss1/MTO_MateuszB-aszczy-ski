#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    regex = r'#(\d+)?(\.)?(\d+)?k'
    shouldDo=True
    param = param.swapcase()
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(regex, format_string[idx:])
                min = result.group(1)
                dot = result.group(2)
                max = result.group(3)
                if not min and not max:
                    print(param,end="")
                elif not min and max and dot:
                    maxInt = int(max)
                    print(f'{param:.{maxInt}}',end="")
                elif min and not max and not dot:
                    minInt = int(min)
                    print(f'{param:>{minInt}}',end="")
                elif min and max and dot:
                    minInt = int(min)
                    maxInt = int(max)
                    print(f'{param:>{minInt}.{maxInt}}',end="")
                else:
                    break
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'k':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
