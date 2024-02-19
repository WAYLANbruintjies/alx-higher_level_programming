#!/usr/bin/python3
"""8. Rectangle"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raise exception, not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        TypeError: If value is not an integer
        ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
