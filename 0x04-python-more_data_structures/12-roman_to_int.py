#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    else:
        sum = 0
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            if len(roman_string) == 1:
                sum = dictionary[i]
            for j in range(len(roman_string) - 1):
                if roman_string[j] > roman_string[j + 1]:
                    sum = sum + dictionary[i]
                elif roman_string[j] < roman_string[j + 1]:
                    sum = list(dictionary)[i + 1] - dictionary[i]
        return sum
