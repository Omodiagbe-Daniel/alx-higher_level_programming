#!/usr/bin/python3
"""defines new_attribute function"""


def add_attribute(cls, attr_name="", attr=""):
    """add new attributes"""
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(cls, attr_name, attr)
