#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    """finds peak in a list of unsorted list"""
    leng = len(list_of_integers)
    if leng == 0:
        return
    elif leng == 1:
        return list_of_integers[0]
    else:
        new_list = list_of_integers
        new_list.sort()
        return new_list[-1]
