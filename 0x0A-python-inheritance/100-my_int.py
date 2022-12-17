#!/usr/bin/python3
"""defines class MyInt"""


class MyInt(int):
    """inherits from built-in class int"""
    def __eq__(self, x):
        """overriding __eq__"""
        if type(x) == int:
            return False

    def __ne__(self, y):
        """overriding __ne__"""
        if type(y) == int:
            return True
