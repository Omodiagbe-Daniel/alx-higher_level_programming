#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    x = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=' ')
        if (x != len(matrix) - 1):
            print()
            x += 1

if __name__ == "__main__":
    print_matrix_integer()
