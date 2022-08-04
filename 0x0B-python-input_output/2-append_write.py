#!/usr/bin/python3
"""appends a string"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added"""

    with open(filename, 'a', encoding="utf-8") as myfile:
        return(myfile.write(text))
