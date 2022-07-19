#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """ a class with private attribute size"""

    def __init__(self, size=0):
        """instantiation with size of type int"""

        self.__size = size

    def area(self):
        return self.__size * self.__size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
