#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_new = list(a_dictionary.keys())
    list_new.sort()
    for i in list_new:
        print("{}: {}".format(i, a_dictionary.get(i)))
