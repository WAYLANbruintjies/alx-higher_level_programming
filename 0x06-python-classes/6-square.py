#!/usr/bin/python3
"""Square class defined"""


class Square:
    """Square class initialisation"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor with size & position = 0
        Args:
            size of type int: The size of the new square
            square position within Tupple
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter & Getter of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position MUST be a tuple of 2 positive+ int")
        self.__position = value

    @property
    def position(self):
        """Setter & Getter for position of square"""
        return (self.__position)

    def my_print(self):
        """STDOUT of square with the value of type char"""
        if self.__size == 0:
            print("")
            return

    def area(self):
        """Return final area of square"""
        return (self.__size * self.__size)

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
