#!/usr/bin/python3
#Prints all integers of a list in reverse order.

def print_reversed_list_integer(my_list=[]):
     if isinstance(my_list, list):
         my_list.reverse()
         for n in my_list:
             print("{}".format(n))
