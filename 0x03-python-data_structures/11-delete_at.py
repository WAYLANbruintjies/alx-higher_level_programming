#!/usr/bin/python3
# File: 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """A function that deletes the item at a specific position in a list."""
    list_len = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > list_len -1:
        return (my_list)
    del my_list[idx]
    return (my_list)
