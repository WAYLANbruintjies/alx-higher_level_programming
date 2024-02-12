#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        if height < 0:
            raise ValueError except("height must be >= 0")
        if width < 0:
            raise ValueError except("width must be >= 0")
