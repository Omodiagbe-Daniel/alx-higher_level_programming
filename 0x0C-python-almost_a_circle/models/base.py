#!/usr/bin/python3
"""Base module"""


class Base:
    """This will be the base for other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialiazation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
