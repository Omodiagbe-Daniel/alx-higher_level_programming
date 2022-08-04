#!/usr/bin/python3
"""JSON represention:"""

import json


def class_to_json(obj):
    """return dictionary discription with simple data structure
        (list, dictionary, string and boolean) for JSON serialization
        of an object"""

    return json.dumps(obj.__dict__)
