#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    count = 0
    for i in range(len(my_list)):
        count += 1
    if idx < 0 or idx > count - 1:
        return my_list
    else:
        new_list = my_list[:idx] + [element] + my_list[idx+1:]
        return new_list
