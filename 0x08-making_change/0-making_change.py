#!/usr/bin/python3
""" Module that contain makeChange
"""
import sys


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
    coins (list of int): A list of the values of the coins in your possession.
    total (int): The total amount to be made with the coins.

    Returns:
    int: The fewest number of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0

    # Initialize the dp array
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0  # Base case: No coins needed to make a total of 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                subres = dp[i - coin]
                if subres != sys.maxsize and subres + 1 < dp[i]:
                    dp[i] = subres + 1

    return -1 if dp[total] == sys.maxsize else dp[total]
