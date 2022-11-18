#!/usr/bin/python3
"""Base module"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dict"""
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
