#!/usr/bin/python3
# File: 2-replace_in_list.py

def element_at(my_list, idx):
    """a function that retrieves an element from a list like in C"""
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
