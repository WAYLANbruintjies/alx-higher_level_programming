#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dir = a_dictionary.copy()
    key_list = list(a_dir.keys())

    for i in key_list:
        a_dir[i] *= 2

    return (a_dir)
