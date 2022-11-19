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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(4, 6)
        elif cls.__name__ == "Square":
            dummy = Square(7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                cls_list = cls.from_json_string(file.read())
        except:
            return []
        new_instances = []
        for obj in cls_list:
            instance = cls.create(**obj)
            new_instances.append(instance)
        return new_instances
