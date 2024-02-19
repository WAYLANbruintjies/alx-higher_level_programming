#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self.copy()))
