#!/usr/bin/env python3

import sys
import re

def transform(numberString):
    outputText = []
    mode = 1;
    for x in numberString:
        if x == '.':
            outputText.append('.')
            mode = 2;
        if x == '0':
            if mode == 1:
                outputText.append('a')
            else:
                outputText.append((0+5)%10)
        elif x == '1':
            if mode == 1:
                outputText.append('b')
            else:
                outputText.append((1+5)%10)
        elif x == '2':
            if mode == 1:
                outputText.append('c')
            else:
                outputText.append((2+5)%10)
        elif x == '3':
            if mode == 1:
                outputText.append('d')
            else:
                outputText.append((3+5)%10)
        elif x == '4':
            if mode == 1:
                outputText.append('e')
            else:
                outputText.append((4+5)%10)
        elif x == '5':
            if mode == 1:
                outputText.append('f')
            else:
                outputText.append((5+5)%10)
        elif x == '6':
            if mode == 1:
                outputText.append('g')
            else:
                outputText.append((6+5)%10)
        elif x == '7':
            if mode == 1:
                outputText.append('h')
            else:
                outputText.append((7+5)%10)
        elif x == '8':
            if mode == 1:
                outputText.append('i')
            else:
                outputText.append((8+5)%10)
        elif x == '9':
            if mode == 1:
                outputText.append('j')
            else:
                outputText.append((9+5)%10)
    out = ''.join(str(e) for e in outputText)
    return out.lower()


def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#[.]+?(\d+)?h'
    floatNum = float(param)
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    print(format_string[idx],end="")
                    continue
                
                precision = result.group(1)
                if precision:
                    precisionInt = int(precision)
                    output = f'{floatNum:.{precisionInt}f}'
                output = transform(output)
                print(output,end="")
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'h':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
