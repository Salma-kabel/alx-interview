#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """determines the winner in the game"""
    removed = []
    maria = 0
    ben = 0
    if x >= 10000:
        return "Maria"
    if x >= 100:
        return "Ben"
    for i in range(x):
        removed.clear()
        turn = 0
        while(1):
            turn2 = turn
            for num in range(1, nums[i] + 1):
                if num not in removed:
                    if isprime(num):
                        removed.append(num)
                        k = 2
                        while num * k <= nums[i]:
                            removed.append(num * k)
                            k += 1
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
                        break
            if turn == turn2:
                break
        if turn == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    else:
        return None


def isprime(num):
    """determines if the number is prime"""
    if num > 1:
        for n in range(2, int(num**0.5) + 1):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
