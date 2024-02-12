#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialising rectangle"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Private instance attribute: width"""
            return self.__width

        @property
        def height(self):
            """Private instance attribute: height"""
            return self.__height

        @width.setter
        def width(self, vale):
            """Sets the width of a rectangle"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @height.setter
            def height(self, value)
            """Sets the height of a rectangle"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
