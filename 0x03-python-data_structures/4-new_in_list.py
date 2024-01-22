#!/usr/bin/python3
# File: 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific index/position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        copy = [i for i in my_list]
        copy[idx] = element
        return (copy)
