#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    def transform(number_string):
        output_text = []
        for x in number_string:
            if x == 'a':
                output_text.append('g')
            elif x == 'b':
                output_text.append('h')
            elif x == 'c':
                output_text.append('i')
            elif x == 'd':
                output_text.append('j')
            elif x == 'e':
                output_text.append('k')
            elif x == 'f':
                output_text.append('l')
            elif x == '0':
                output_text.append('o')
            else:
                output_text.append(x)
        out = ''.join(str(e) for e in output_text)
        return out

    shouldDo=True
    done = False
    regex = r'#[.]+?(\d+)?j'
    regex2 = r'#j'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    result = re.search(regex2, format_string[idx:])
                    if result:
                        output = transform(param)
                        print(output,end="")
                        done = True
                        shouldDo = False
                        continue
                    print(format_string[idx],end="")
                    continue

                min = result.group(1)
                fillChar = '0'
                output = param
                if min:
                    minInt = int(min)
                    output = output.rjust(minInt, fillChar) 
                output = transform(output)
                print(output,end="")
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'j':
                shouldDo=True
    print("")


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())

