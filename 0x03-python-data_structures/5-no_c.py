#!/usr/bin/python3
"""removes all c and C character"""


def no_c(my_string):
    mystr = ""
    for i in my_string:
        if i != "c" and i != "C":
            mystr = mystr + i
    return mystr


if __name__ == "__main__":
    no_c()
