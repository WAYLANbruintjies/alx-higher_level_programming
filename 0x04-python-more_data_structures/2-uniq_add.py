#!/usr/bin/python3
#File: 2-uniq_add.py

"""function that adds all unique integers in a list (only once for each integer)"""
def uniq_add(my_list=[]):
    uni_list = set(my_list)
    nums = 0

    for i in uni_list:
        nums += i

    return (nums)
