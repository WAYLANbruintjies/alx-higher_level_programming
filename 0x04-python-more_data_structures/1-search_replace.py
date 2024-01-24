#!/usr/bin/python3
#File: 1-search_replace.py

"""A function that replaces all occurrences of an element by another in a new list"""
def search_replace(my_list, search, replace):
    _new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (_new_list)
