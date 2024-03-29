#!/usr/bin/python3
"""1. Base class"""


class Base():
    """A class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
