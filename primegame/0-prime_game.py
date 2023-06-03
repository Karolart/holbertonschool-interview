#!/usr/bin/python3

"""
Defines function that determines the winner after a certain number of rounds
of playing the Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a game played for multiple rounds.

    Args:
        x (int): Number of rounds to be played.
        nums (list): Array of 'n' values for each round.

    Returns:
        str or None: The name of the player that won the most rounds ('Maria' or 'Ben'),
        or None if the winner cannot be determined.
    """

    def isPrime(num):
        """
        Checks if a number is prime.

        Args:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def playGame(n, isMariaTurn):
        """
        Simulates the game for a given number 'n' and player's turn.

        Args:
            n (int): The current number.
            isMariaTurn (bool): True if it's Maria's turn, False otherwise.

        Returns:
            bool: True if the current player can force a win, False otherwise.
        """
        if n == 1:  # Base case: No prime numbers left to choose
            return not isMariaTurn

        for i in range(2, n + 1):
            if isPrime(i):
                # Remove the prime number and its multiples
                new_nums = [num for num in range(1, n + 1) if num % i != 0]
                # Recursively play the game with the updated numbers and next player's turn
                if not playGame(len(new_nums), not isMariaTurn):
                    return True

        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if playGame(n, True):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
    
