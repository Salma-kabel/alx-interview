#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """determines the winner in the game"""
    removed = []
    winner = []
    for i in range(x):
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
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
                        break
            if turn == turn2:
                break
        if turn == 0:
            winner.append(1)
        else:
            winner.append(0)
    maria = 0
    ben = 1
    for i in range(len(winner)):
        if winner[i] == 0:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    else:
        return None

def isprime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
