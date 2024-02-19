#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited of a given class
    and returns a boolean of an instance
    """
    if isinstance(obj, a_class):
        return True
    return False
