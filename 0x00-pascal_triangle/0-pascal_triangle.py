#!/usr/bin/python3
"""function that implements pascal triangle"""


def pascal_triangle(n):
    """implementation of pascal's triangle"""
    arr = []
    for i in range(0, n):
        arr2 = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                arr2.append(1)
            else:
                arr2.append(arr[i - 1][j - 1] + arr[i - 1][j])
        arr.append(arr2)
    return arr
