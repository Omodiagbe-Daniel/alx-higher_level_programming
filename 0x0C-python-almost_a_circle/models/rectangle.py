#!/usr/bin/python3
"""rectangle class"""

from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""
    @property
    def width(self):
        return self.__val

    @width.setter
    def width(self, val):
        if type(val) not in (int, float):
            raise TypeError("width must be a number")
            return
        if val < 0:
            raise ValueError("number must be 0 or greater than 0")
            return
        self.__val = val

    @property
    def height(self):
        return self.__val

    @height.setter
    def height(self, val):
        if type(val) not in (int, float):
            raise TypeError("height must be a number")
            return
        if val < 0:
            raise ValueError("number must be 0 or greater than 0")
            return
        self.__val = val

    @property
    def x(self):
        return self.__val

    @x.setter
    def x(self, val):
        if type(val) not in (int, float):
            raise TypeError("x must be a number")
            return
        if val < 0:
            raise ValueError("number must be 0 or greater than 0")
            return
        self.__val = val

    @property
    def y(self):
        return self.__val

    @y.setter
    def y(self, val):
        if type(val) not in (int, float):
            raise TypeError("y must be a number")
            return
        if val < 0:
            raise ValueError("number must be 0 or greater than 0")
            return
        self.__val = val

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
