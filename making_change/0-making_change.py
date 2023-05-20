#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed

    Args:
        coins (list): A list of coin values available.
        total (int): The desired total value.

    Returns:
        int: The fewest number of coins needed to reach the total.
        Returns -1 if the total cannot be met.

    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update the number of coins needed for each total value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins needed for the total
    return dp[total]
