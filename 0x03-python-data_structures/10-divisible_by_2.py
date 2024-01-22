#!/usr/bin/python3
# File: 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list."""
    multiples = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
