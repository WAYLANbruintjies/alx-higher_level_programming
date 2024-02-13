#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """Adds 2 integers"""
    if not isinstance(a, int or float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int or float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
