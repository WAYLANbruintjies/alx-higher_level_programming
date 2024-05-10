#!/usr/bin/python3
"""
Algorithm question, Technical interview prep - find the peak in an unsorted integer list.
Prototype: def find_peak(list_of_integers):
"""

def find_peak(list_of_integers):
    """Function that finds a peak in a list on unsorted ints"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
