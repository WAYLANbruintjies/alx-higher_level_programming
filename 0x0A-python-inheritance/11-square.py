#!/usr/bin/python3
"""10. Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
