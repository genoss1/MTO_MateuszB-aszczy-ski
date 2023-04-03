#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    REGEX = r'#(\d+)?g'
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(REGEX, format_string[idx:])
                firstdigit = result.group(1)
                if firstdigit:
                    firstdigitInt = int(firstdigit)
                    print(f'{param:>{firstdigitInt}}',end="")
                else:
                    break
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'g':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
