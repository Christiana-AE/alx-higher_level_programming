#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_array = []
    count = 0
    for i in range(len(my_list)):
        if my_list[i] not in new_array:
            new_array.append(my_list[i])
            continue

    for i in range(len(new_array)):
        count += new_array[i]
    return count
