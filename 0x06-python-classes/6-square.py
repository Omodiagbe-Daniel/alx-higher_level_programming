#!/usr/bin/python3
""" a class based on 5-square.py"""


class Square:
    """a class square that prints out
       a square using # along side it position
    """
    def __init__(self, size=0, position=(0, 0)):
        """"initialization of attribues"""

        self.size = size
        self.position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            if self.__position[1] >= 0:
                print(" " * self.__position[0], end='')
            for j in range(self.__size):
                print("#", end='')
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
