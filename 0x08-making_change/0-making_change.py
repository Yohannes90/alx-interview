#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp table for all amounts that can be reached with the current coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met with the given coins
    return dp[total] if dp[total] != float('inf') else -1
