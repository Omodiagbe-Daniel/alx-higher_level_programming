#!/usr/bin/python3


def max_integer(my_list=[]):
    maxi = my_list[0]
    i = 0
    if my_list == []:
        return None
    for i in range(len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]
    return maxi
