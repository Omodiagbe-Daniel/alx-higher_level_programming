#!/usr/bin/python3
"""adding two integers"""


def add_integer(a, b=98):
    """function that adds two integers"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
