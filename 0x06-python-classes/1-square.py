#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Representation a square"""

    def __init__(self, size):
        """Initialise a new Square with a private instance attibute
        Args:
            size of type int: The size of the new square.
            """

        self.__size = size
