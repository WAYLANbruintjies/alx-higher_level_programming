#!/usr/bin/python3
# File: 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Prints a list of all the integers within the list"""
    for n in range(len(my_list)):
        print("{:d}".format(my_list[n]))
