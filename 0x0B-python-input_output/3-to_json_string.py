#!/usr/bin/python3
"""JSON representation"""


import json
"""importing json module"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
