#!/usr/bin/python3
"""function to solve the N queens problem"""


from sys import argv


def main():
    """solves n queen problem"""
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        num = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if int(argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    arr = []
    arr1 = []
    length = int(argv[1])
    row(0, arr1, arr, length)
    for w in range(len(arr)):
        print(arr[w])


def row(rw, arr1, arr, length):
    if rw == length:
        arr.append(arr1.copy())
        return
    for j in range(length):
        if valid(arr1, rw, j):
            arr1.append([rw, j])
            row(rw + 1, arr1, arr, length)
            arr1.pop()


def valid(arr1, j, m):
    cl = j
    k = m
    flag = True
    while cl > 0 and k > 0:
        for w in range(len(arr1)):
            if arr1[w][0] == cl - 1 and arr1[w][1] == k - 1:
                flag = False
                break
        if not flag:
            return 0
        k -= 1
        cl -= 1
    k = m
    cl = j
    while cl > 0 and k < int(argv[1]):
        for w in range(len(arr1)):
            if arr1[w][0] == cl - 1 and arr1[w][1] == k + 1:
                flag = False
                break
        if not flag:
            return 0
        k += 1
        cl -= 1
    k = m
    cl = j
    while cl > 0:
        for w in range(len(arr1)):
            if arr1[w][0] == cl - 1 and arr1[w][1] == m:
                flag = False
                return 0
        if not flag:
            break
        cl -= 1
    return 1


if __name__ == "__main__":
    main()
