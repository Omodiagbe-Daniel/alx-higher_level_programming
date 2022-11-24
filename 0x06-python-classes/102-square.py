#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """ a class with private attribute size"""

    def __init__(self, size=0):
        """instantiation with size of type int"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(self.__size) not in (float, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """instantiation with size of type int"""

        self.__size = size

    def area(self):
        a = self.__size * self.__size
        return a


    def __lt__(self, x):
        return self.area() < x.area()

    def __ge__(self, x):
        return self.area() >= x.area()

    def __le__(self, x):
        return self.area() <= x.area()

    def __gt__(self, x):
        return self.area() > x.area()

    def __ne__(self, x):
        return self.area() != x.area()

    def __eq__(self, x):
        return self.area() == x.area()

