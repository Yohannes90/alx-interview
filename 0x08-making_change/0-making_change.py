#!/usr/bin/python3
import sys


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # list to store the minimum number of coins for each amount of total
    dp = [sys.maxsize for _ in range(total + 1)]
    dp[0] = 0  # Base case: No coins needed to make a total of 0

    # Number of different coin denominations
    m = len(coins)

    # Fill the dp table in a bottom-up manner
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = dp[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < dp[i]:
                    dp[i] = subres + 1

    # If dp[total] still sys.maxsize, then total can't be met with given coins
    return -1 if dp[total] == sys.maxsize else dp[total]
