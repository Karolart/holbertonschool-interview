#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""

def pascal_triangle(n):

    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    triangle = []
    if n <= 0:
        return triangle
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):

            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
