#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        x = 0
        for j in range(len(matrix[i])):
            if x < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
            x += 1
        print()


if __name__ == "__main__":
    print_matrix_integer()