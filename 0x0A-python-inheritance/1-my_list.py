#!/usr/bin/python3
"""1. My list, File: 1-my_list.py"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
