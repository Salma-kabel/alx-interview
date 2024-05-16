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
    for i in range(int(argv[1])):
        arr1 = []
        m = -2
        j = 0
        while j < int(argv[1]):
            m += 1
            flag = True
            if j == 0:
                arr1.append([0, i])
            else:
                k = m
                cl = j
                while k > 0 and cl > 0:
                    for w in range(len(arr1)):
                        if arr1[w][0] == cl - 1 and arr1[w][1] == k - 1:
                            flag = False
                    if not flag:
                        break
                    k -= 1
                    cl -= 1
                k = m
                cl = j
                while cl > 0 and k < int(argv[1]):
                    for w in range(len(arr1)):
                        if arr1[w][0] == cl - 1 and arr1[w][1] == k + 1:
                            flag = False
                    if not flag:
                        break
                    k += 1
                    cl -= 1
                k = m
                cl = j
                while cl > 0:
                    for w in range(len(arr1)):
                        if arr1[w][0] == cl - 1 and arr1[w][1] == m:
                            flag = False
                    if not flag:
                        break
                    cl -= 1
                if not flag:
                    while m == int(argv[1]) - 1 and j > 1:
                        j -= 1
                        m = arr1[-1][1]
                        arr1.pop()
                    if m == int(argv[1]) - 1 and j == 1:
                        break
                    continue
                arr1.append([j, m])
                m = -1
            j += 1
        if (len(arr1) == int(argv[1])):
            arr.append(arr1)
    for w in range(len(arr)):
        print(arr[w])


if __name__ == "__main__":
    main()
