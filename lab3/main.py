#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    REGEX = r'#(\d+)?(\.)?(\d+)?k'
    shouldDo=True
    param = param.swapcase()
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(REGEX, format_string[idx:])
                firstdigit = result.group(1)
                dot = result.group(2)
                seconddigit = result.group(3)
                if not firstdigit and not seconddigit:
                    print(param,end="")
                elif firstdigit and seconddigit and dot:
                    firstdigitInt = int(firstdigit)
                    seconddigitInt = int(seconddigit)
                    print(f'{param:>{firstdigitInt}.{seconddigitInt}}',end="")
                elif firstdigit and not seconddigit and not dot:
                    firstdigitInt = int(firstdigit)
                    print(f'{param:>{firstdigitInt}}',end="")
                elif not firstdigit and seconddigit and dot:
                    seconddigitInt = int(seconddigit)
                    print(f'{param:.{seconddigitInt}}',end="")
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
