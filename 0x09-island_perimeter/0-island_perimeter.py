#!/usr/bin/python3
"""island parameter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    length = len(grid)
    arr = len(grid[0])
    count = 0
    for i in range(length):
        for j in range(arr):
            if grid[i][j] == 1:
                if i > 0 and grid[i - 1][j] == 0:
                    count += 1
                if i < length - 1 and grid[i + 1][j] == 0:
                    count += 1
                if j > 0 and grid[i][j - 1] == 0:
                    count += 1
                if j < arr - 1 and grid[i][j + 1] == 0:
                    count += 1
    return count
