#!/usr/bin/python3
""" inherits from BaseGeometry"""


class BaseGeometry:
    """" adding a public instance method """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        self.name = name
        self.__value = value


class Rectangle(BaseGeometry):
    """Instantiation with width and height:
       def __init__(self, width, height):
       width and height must be private.
       No getter or setterwidth and height must be positive integers,
       validated by integer_validator"""

    def __init__(self, width, height):
        self.integer_validator("idth", width)
        self.integer_validator("height", height)
