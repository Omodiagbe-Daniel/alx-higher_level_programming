#!/usr/bin/python3
"""square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """square representation"""
        return (f"[Square] {self.__size}/{self.__size}")
