#!/usr/bin/python3
"""matrix rotation"""


def rotate_2d_matrix(matrix):
    """rotate matrix 90 degree clockwise"""
    matrix2 = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix2[i][j] = matrix[i][j]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix2[len(matrix) - 1 - j][i]
