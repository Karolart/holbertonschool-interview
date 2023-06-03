#!/usr/bin/python3

"""
   Maria always goes first and both players play optimally,
   determine who the winner of each game is.
"""


def isWinner(x, nums):
    # Define a helper function to check if a number is prime
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Define the recursive game function
    def playGame(n, isMariaTurn):
        # Base case: If n = 1, the current player loses
        if n == 1:
            return not isMariaTurn

        # Iterate through the remaining numbers and choose a prime
        for i in range(2, n + 1):
            if isPrime(i):
                # Remove the prime number and its multiples
                new_nums = [num for num in range(1, n + 1) if num % i != 0]
                # Recursively play the game with the updated numbers and next player's turn
                if not playGame(len(new_nums), not isMariaTurn):
                    return True

        return False

    # Count the number of wins for each player
    maria_wins = 0
    ben_wins = 0

    # Play the game for each round
    for n in nums:
        if playGame(n, True):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner or return None if it cannot be determined
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
