#!/usr/bin/python3
"""Minimum Operations"""


def Factorization(x):
    """Returns elements of x"""
    div = 2
    array = list()
    while (div <= x):
        if x % div == 0:
            array.append(div)
            x /= div
        else:
            div += 1

    return array


def minOperations(n):
    """Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""
    min = 0
    factors = [x for x in Factorization(n)]
    occurences = {item: factors.count(item) for item in factors}
    for k, v in occurences.items():
        min += k * v
    return min
