#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    REGEX = r'#(\d+)?j'
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(REGEX, format_string[idx:])
                firstdigit = result.group(1)
                if firstdigit and param.isdigit():
                    firstdigitInt = int(firstdigit)
                    param = int(param)
                    nowa_liczba = hex(param)[2:].replace('a', 'g').replace('b', 'h').replace('c', 'i').replace('d', 'j').replace('e', 'k').replace('f', 'l')
                    print(f'{nowa_liczba:>{firstdigitInt}}',end="")
                elif not firstdigit and param.isdigit():
                    param = int(param)
                    nowa_liczba = hex(param)[2:].replace('a', 'g').replace('b', 'h').replace('c', 'i').replace('d', 'j').replace('e', 'k').replace('f', 'l')
                    print(f'{nowa_liczba}',end="")
                elif firstdigit and not param.isdigit():
                    firstdigitInt = int(firstdigit)
                    print(f'{param:>{firstdigitInt}}',end="")
                else:
                    break
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'j':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
