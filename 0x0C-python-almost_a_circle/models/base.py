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

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON str represenation to a file"""
        list_obj = []
        if list_objs is None:
            list_obj = []
        else:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                list_obj.append(json_dict)

        with open(f"{cls.__name__}.json", "w") as file:
            json.dump(list_obj, file)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        json_list = []
        if json_string is None:
            return json_list
        else:
            return json.loads(json_string)
