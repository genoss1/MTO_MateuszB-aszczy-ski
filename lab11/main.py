#!/usr/bin/env python3

import sys

def new_number(old_number):
    new_number = int((old_number * 2) / len(str(old_number)))
    if new_number % 2 != 0:
        return str(hex(new_number)).replace('0x', '')
    return str(new_number)


def my_printf(format_string, param):
    if '#a' not in format_string:
        print(format_string)
        return

    replace = '#a'

    try:
        param = int(param)
    except Exception:
        param = 0

    replace_with = new_number(param)

    print(format_string.replace(replace, replace_with))


data = sys.stdin.readlines()


for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[ i + 1].rstrip())
