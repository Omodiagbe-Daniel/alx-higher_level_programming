#!/usr/bin/python3


""" inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height:
       def __init__(self, width, height):
       width and height must be private.
       No getter or setterwidth and height must be positive integers,
       validated by integer_validator"""

    def __init__(self, width, height):
        self.width = __width
        self.height = __height
    def integer_validator(self):
        if type(self.width) == int and self.width > 0:
            return self.width
        if type(self.height) == int and self.height > 0:
            return self.height
