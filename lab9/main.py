#!/usr/bin/env python3

import sys

def is_number(x):
    return x.isnumeric()

def num_to_letter(x):
    if x == '0':
        return 'a'
    if x == '1':
        return 'b'
    if x == '2':
        return 'c'
    if x == '3':
        return 'd'
    if x == '4':
        return 'e'
    if x == '5':
        return 'f'
    if x == '6':
        return 'g'
    if x == '7':
        return 'h'
    if x == '8':
        return 'i'
    if x == '9':
        return 'j'

def new_digit(y):
    try:
        x = int(y)
        return str((x+5)%10)
    except:
        return y


def float_dot(param, l):
    ret = ""
    i = 0
    while (not (param[i] == '.')) and i < len(param):
        ret = ret + num_to_letter(param[i])
        i = i + 1

    i = i + 1
    ret = ret + '.'
    w = 0

    while w < l - 1:
        if (i < len(param)):
            ret = ret + new_digit(param[i])
        else:
           ret = ret + new_digit(0)
        i = i + 1
        w = w + 1

    if (i + 1 < len(param)):
        if (int(param[i+1]) >= 5):
            ret = ret + new_digit(str(int(param[i])+1))
        else:
            ret = ret + new_digit(param[i])
    elif (i < len(param)):
        ret = ret + new_digit(param[i])
    else:
        ret = ret + new_digit(0)

    
    return ret

def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string)):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and is_number(format_string[idx+2]):
                i = idx + 3
                num = int(format_string[idx+2])
                filler = "o"

                while is_number(format_string[i]):
                    num *= 10
                    num += int(format_string[i])
                    i += 1
                
                if format_string[i] == 'h':
                    print(float_dot(param, num),end="")
                    skip = i - idx   
                else:
                    print(format_string[idx],end="")
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
