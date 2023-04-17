#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#.(\d+)?g'

    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                minus = False
                result = re.search(regex, format_string[idx:])
                if not result:
                    break
                min = result.group(1)
                fillChar = '0'
                if(int(param) < 0):
                    minus = True
                    output = str(int( param[1:]) )
                    nowa_liczba = ""
                    for cyfra in output:
                        nowa_liczba += str((int(cyfra)*9+1)%10)
                else:
                    output = str(int(param))
                    nowa_liczba = ""
                    for cyfra in output:
                        nowa_liczba += str((int(cyfra)*9+1)%10)
                if min:
                    minInt = int(min)
                    nowa_liczba = nowa_liczba.rjust(minInt, fillChar) 
                if(minus):
                    print('-',end="")
                print(nowa_liczba,end="")
                done = True
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")

        else:
            if(format_string[idx] == 'g'):
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
