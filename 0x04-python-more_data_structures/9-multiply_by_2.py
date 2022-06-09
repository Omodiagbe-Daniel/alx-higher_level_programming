#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    for i, v in a_dictionary.items():
        new_dict[i] = v * 2
    return new_dict
