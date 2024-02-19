#!/usr/bin/python3
"""7. Integer validator"""


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
