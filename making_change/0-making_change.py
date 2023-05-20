#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # list to track the fewest number of coins 
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update the number of coins needed for each total value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins
    return dp[total]
