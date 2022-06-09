#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    else:
        sum = 0
        dictionary = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        for i, v in dictionary.items():
            if i in roman_string:
                sum += v
        return sum
