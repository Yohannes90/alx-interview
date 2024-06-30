#!/usr/bin/python3
""" Module for UTF-8 Validation.
"""


def validUTF8(data):
    """ Check if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): A list of integers representing the data to be checked.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    byte_count = 0

    for num in data:
        if byte_count == 0:
            if (num >> 5) == 0b110:
                byte_count = 1
            elif (num >> 4) == 0b1110:
                byte_count = 2
            elif (num >> 3) == 0b11110:
                byte_count = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            byte_count -= 1

    return byte_count == 0
