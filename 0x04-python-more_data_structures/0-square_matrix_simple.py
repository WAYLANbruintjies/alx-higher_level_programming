#!/usr/bin/python3
#0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """A function that computes the square value of all integers of a matrix"""
    new_matrix = matix.copy()

     for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
