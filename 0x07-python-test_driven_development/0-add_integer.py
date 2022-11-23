#!/usr/bin/python3
"""adding two integers"""


def add_integer(a, b=98):
    """function that adds two integers"""

    if a == float('NaN') or a == float('inf'):
        raise TypeError("a must be an integer")
    if b == float('NaN') or b == float('inf'):
        raise TypeError("b must be an integer")
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
