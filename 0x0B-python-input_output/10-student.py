#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student():
    """
    A student class with public instances
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if (type(attrs) == list and
                all(type(items) == str for items in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
