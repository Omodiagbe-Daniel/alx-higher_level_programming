#!/usr/bin/python3


def max_integer(my_list=[]):
    maxi = 0
    i = 0
    if my_list == []:
        return None
    else:
        len1 = len(my_list) - 1
        while my_list[i] < my_list[len1]:
            if my_list[i+1] > my_list[i]:
                maxi = my_list[i+1]
            else:
                maxi = my_list[i]
            i += 1
    return maxi
