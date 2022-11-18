#!/usr/bin/python3
"""rectangle class"""

from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not (int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """function to calculate area"""
        return self.height * self.width

    def display(self):
        """prints a rectangle using #"""
        if self.y != 0:
            print("\n" * (self.y - 1))
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updates the class"""
        if args:
            if len(args) < 1:
                return
            else:
                self.id = args[0]
            if len(args) < 2:
                return
            else:
                self.width = args[1]
            if len(args) < 3:
                return
            else:
                self.height = args[2]
            if len(args) < 4:
                return
            else:
                self.x = args[3]
            if len(args) < 5:
                return
            else:
                self.y = args[4]
            return
        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
