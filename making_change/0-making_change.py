#!/usr/bin/python3
"""Making Change"""

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to reach a given total using a given set of coins.

    Args:
        coins (list): A list of coin values available.
        total (int): The desired total value.

    Returns:
        int: The fewest number of coins needed to reach the total. Returns -1 if the total cannot be met.

    """

    if total <= 0:
        return 0

    # Initialize a list to track the fewest number of coins needed for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update the number of coins needed for each total value
        for i in range(coin, total + 1):
            # Choose the minimum between the current number of coins needed and the number of coins needed
            # to reach the current total minus the coin value, plus one coin of the current value.
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the final total is still infinity, it means it cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins needed for the total
    return dp[total]
