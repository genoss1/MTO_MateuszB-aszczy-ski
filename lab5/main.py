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
                if firstdigit and param.isdigit:
                    firstdigitInt = int(firstdigit)
                    nowa_liczba = ""
                    for cyfra in param:
                        if cyfra == "0":
                            nowa_liczba += "9"
                        else:
                            nowa_liczba += str(int(cyfra)-1)
                    print(f'{nowa_liczba:>{firstdigitInt}}',end="")
                elif firstdigit and not param.isdigit:
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
