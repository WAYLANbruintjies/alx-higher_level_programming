#!/usr/bin/python3
"""8. Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
