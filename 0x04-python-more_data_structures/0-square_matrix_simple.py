#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_square = []
    for i in (matrix):
        square = list(map(lambda x: x**2, i))
        new_square.append(square)
    return new_square
