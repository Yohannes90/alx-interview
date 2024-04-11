#!/usr/bin/python3
""" function outputting Pascal’s triangle represention for n
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing Pascal’s triangle of n
    """
    if n <= 0:  # Edge case handling
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            for j in range(1, i):
                # Calculate each element of the row based on the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    return triangle
