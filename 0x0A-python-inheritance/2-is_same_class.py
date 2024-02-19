#!/usr/bin/python3
"""2. Exact same object"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class
    and returns boolean of an instance of a_class
    """
    if type(obj) == a_class:
        return True
    return False
