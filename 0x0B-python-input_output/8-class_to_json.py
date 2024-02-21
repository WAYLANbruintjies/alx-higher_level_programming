#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """
    Returns the dictionary for JSON serialization of object
    """
    return obj.__dict__
