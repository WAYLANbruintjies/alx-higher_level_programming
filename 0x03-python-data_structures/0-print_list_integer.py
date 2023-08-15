#!/usr/bin/python3
#Prints all integers of a list

def print_list_integer(my_list=[]):
    for n in range(len(my_list)):
    print("{:d}".format(my_list[n]))
