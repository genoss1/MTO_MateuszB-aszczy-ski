#!/usr/bin/env python3

import sys


def weird_binary(param):
    binary = bin(param).replace('0b', '')

    changed_binary = ''

    for i, num in enumerate(binary[::-1]):
        if num == '0':
            changed_binary += '0'
        else:
            changed_binary += 'abcdefghij'[(i)%10]

    changed_binary = changed_binary[::-1]

    return changed_binary


def my_printf(format_string, param):
    replace = '#b'
    if replace not in format_string:
        print(format_string)
        return

    try:
        param = int(param)
    except Exception:
        param = 0

    replace_with = weird_binary(param)

    print(format_string.replace(replace, replace_with))


data = sys.stdin.readlines()


for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[ i + 1].rstrip())
