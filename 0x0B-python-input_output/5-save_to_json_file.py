#!/usr/bin/oython3
"""JSON representation"""


import json
"""imported json module"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to
       a text file, using a JSON representation"""

    with open(filename, 'w') as myfile:
        return json.dump(my_obj, myfile)
