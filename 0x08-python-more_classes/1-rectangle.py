#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Rectangle class defined"""

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle class instance within constructor
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of a Rectangle > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of a Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of a Rectangle > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
