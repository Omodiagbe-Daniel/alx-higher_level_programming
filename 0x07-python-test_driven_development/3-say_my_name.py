#!/usr/bin/python3
"""prints my name"""


def say_my_name(first_name, last_name=""):
    """a function that prints my name"""

    if type(first_name) is not str or first_name != first_name:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name != last_name:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
