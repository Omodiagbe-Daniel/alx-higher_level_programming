#!/usr/bin/python3


""" checks if an objedct is an instance of a specified type"""


def is_same_class(obj, a_class):

    if type(obj) == a_class:
        return True
    else:
        return False
