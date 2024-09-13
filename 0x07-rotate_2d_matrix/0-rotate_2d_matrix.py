#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The input 2D matrix to be rotated.

    Returns:
        None: The matrix is edited in-place.

    Raises:
        None.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
