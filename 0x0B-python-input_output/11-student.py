#!/usr/bin/python3
"""11. Student to disk and reload"""


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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

    def reload_from_json(self, json):
        for key, val in json.items():
            setattr(self, key, val)
