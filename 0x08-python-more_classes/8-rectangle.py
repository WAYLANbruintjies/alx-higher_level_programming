#!/usr/bin/python3
"""
8. Compare rectangles
"""


class Rectangle:
    """Rectangle class defined"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle)
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle)
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

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
        alt_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                alt_str += str(self.print_symbol)
            alt_str += '\n'
        return alt_str[:-1]

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
        Rectangle.number_of_instances -= 1
