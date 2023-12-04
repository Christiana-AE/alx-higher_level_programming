#!/usr/bin/env python3

def no_c(my_string):
    emptyList = ""
    for i in my_string:
        if (i == 'C' or i == 'c'):
            continue
        emptyList += i
    return emptyList
