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

    should_do = True
    done = False
    regex = r'#[.](\d+)?j'
    for idx in range(0, len(format_string)):
        if should_do:
            if format_string[idx] == '#' and not done:
                result = re.search(regex, format_string[idx:])
                if not result:
                    print(format_string[idx], end="")
                    continue

                min = result.group(1)
                fill_char = '0'
                output = param
                output = transform(output)
                if min:
                    min_int = int(min)
                    output = output.rjust(min_int, fill_char)
                print(output, end="")
                done = True
                should_do = False
            else:
                print(format_string[idx], end="")
        else:
            if format_string[idx] == 'j':
                should_do = True
    print("")


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())

