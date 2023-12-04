#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    listlength = len(my_list) - 1
    for i in range(len(my_list)):
        print('{:d}'.format(my_list[listlength]))
        listlength = listlength - 1
