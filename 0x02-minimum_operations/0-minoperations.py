#!/usr/bin/python3
"""method that calculates the fewest number of operations needed
to result in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
