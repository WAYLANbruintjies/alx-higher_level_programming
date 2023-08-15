#!/usr/bin/python3
#Prints all integers of a list

def print_list_integer(my_list=[]):
    """0. Print a list of integers"""
    for n in range(len(my_list)):
        print("{:d}".format(my_list[n]))
