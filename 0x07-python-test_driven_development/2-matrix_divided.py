#!/usr/bin/python3
"""a matrix function"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        else:
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in (int, float):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
    if len(matrix) > 1 and type(matrix) is list:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    for q in matrix:
        list1 = list(map(lambda x: round((x / div), 2), q))
        new_list.append(list1)
    return new_list
