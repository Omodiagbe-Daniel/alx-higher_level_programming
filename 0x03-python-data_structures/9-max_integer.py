#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxi = sorted(my_list)
    return (maxi[-1])
