#!/usr/bin/python3
"""module that defines Lookedclass"""


class LockedClass:
    """prevents creation of dynamic new instance attributes"""
    __slots__ = ['first_name']
    pass
