#!/usr/bin/python3
""" inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation with width and height:
       def __init__(self, width, height):
       width and height must be private.
       No getter or setterwidth and height must be positive integers,
       validated by integer_validator"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
