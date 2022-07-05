#!/usr/bin/puthon3
"""a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """ a class with private attribute size"""

    def __init__(self, size=0):
        """instantiation with size of type int"""

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
