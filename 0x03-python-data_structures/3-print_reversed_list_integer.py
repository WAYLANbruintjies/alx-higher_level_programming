#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints all integers within a list in reverse order"""
    if isinstance(my_list, list):
        my_list.reverse()
        for n in my_list:
            print("{:d}".format(n))
