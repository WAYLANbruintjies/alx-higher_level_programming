#!/usr/bin/python3
# File: 9-max_integer.py

def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list."""
    if len(my_list) <= 0:
        return (None)
    else:
        biggest = my_list[0]
        for n in range(len(my_list)):
            if my_list[n] > biggest:
                biggest = my_list[n]
        return (biggest)
