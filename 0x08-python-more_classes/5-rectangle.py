#!/usr/bin/python3
"""
2. Area and Perimeter
"""


class Rectangle:
    """Rectangle class defined"""

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns an informal string representation
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        new_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += '#'
            new_str += '\n'
        return new_str[:-1]

    def __repr__(self):
        """
        Return internal string representation of Rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of a Rectangle
            Area = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle
            Perimeter = 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        """
        Deletes a Rectangle
        """
        print("Bye rectangle...")
