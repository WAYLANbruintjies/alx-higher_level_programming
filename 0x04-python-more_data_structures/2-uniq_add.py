#!/usr/bin/python3

def uniq_add(my_list=[]):
    uni_list = set(my_list)
    nums = 0

    for i in uni_list:
        nums += i

    return (nums)
