#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """0. Squared simple"""
    copied_matrix = matix.copy()

     for i in range(len(matrix)):
        copied_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (copied_matrix)
