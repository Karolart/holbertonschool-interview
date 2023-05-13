#!/usr/bin/python3

"""
rotate_matrix.py
A Python script to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of lists): The input 2D matrix.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


if __name__ == '__main__':
    # Test the function with a sample matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Original matrix:")
    for row in matrix:
        print(row)

    rotate_2d_matrix(matrix)

    print("Rotated matrix:")
    for row in matrix:
        print(row)