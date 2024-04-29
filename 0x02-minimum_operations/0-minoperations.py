#!/usr/bin/python3
""" function that calculates the fewest number of operations needed
    to result in exactly n H characters in the file
"""


def minOperations(n):
    """ function that calculates the fewest number of operations needed
        to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start from the smallest divisor (besides 1)

    while n > 1:
        while n % divisor == 0:
            n //= divisor  # Divide n by the divisor
            operations += divisor  # Add divisor to the operations count
        divisor += 1  # Increment divisor for the next iteration

    return operations
