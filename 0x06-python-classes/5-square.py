#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """ a class with private attribute size"""

    def __init__(self, size=0):
        """instantiation with size of type int"""

        self.__size = size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(#, end='')
        print()

    def area(self):
        return self.__size * self.__size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
