#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers\
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return
