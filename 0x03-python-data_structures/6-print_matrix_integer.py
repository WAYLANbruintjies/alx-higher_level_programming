#!/usr/bin/python3
# File: 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers."""
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
