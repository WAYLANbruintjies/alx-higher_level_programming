#!/usr/bin/python3
"""4. Only sub class of"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class
    and returns a boolean
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
