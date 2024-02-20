#!/usr/bin/python3
"""13. Can I?"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
