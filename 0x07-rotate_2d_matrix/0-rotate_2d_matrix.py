#!/usr/bin/python3
"""
Module that contain rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    """
    le, ri = 0, len(matrix) - 1

    while le < ri:
        for i in range(ri - le):
            top, bottom = le, ri
            topLeft = matrix[top][le + i]  # save TL value
            matrix[top][le + i] = matrix[bottom - i][le]  # move BL to TL
            matrix[bottom - i][le] = matrix[bottom][ri - i]  # move BR to BL
            matrix[bottom][ri - i] = matrix[top + i][ri]  # move TR to BR
            matrix[top + i][ri] = topLeft  # move TL to TR
        ri -= 1
        le += 1
