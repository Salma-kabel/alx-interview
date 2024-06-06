#!/usr/bin/python3
"""making change function"""


def makeChange(coins, total):
    """ determine the fewest number of coins needed
    to meet a given amount total"""
    if total <= 0:
        return 0
    s_list = sorted(coins, reverse=True)
    coin = 0
    for val in s_list:
        if val < total:
            num = int(total) / int(val)
            coin = coin + int(num)
            total = total - int(num) * val
    if coin == 0 or total != 0:
        return -1
    return coin
