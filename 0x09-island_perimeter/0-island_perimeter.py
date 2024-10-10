#!/usr/bin/python3

"""
Function to calculate the perimeter of an island in a grid.

The grid is represented by a list of lists
where 0s represent water and 1s represent land.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island.

    Args:
        grid (list of list of int): A list of lists
        where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in idx]

            if grid[i][j]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idx)])

    return (count)
