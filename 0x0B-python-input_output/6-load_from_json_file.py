#!/usr/bin/python3
"""JSON representation"""


import json
"""imported json module"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""

    with open(filename, 'r') as myfile:
        return json.load(myfile)
