#!/usr/bin/python3
from sys import argv


def infinite():
    i = 1
    sum = 0
    count = len(argv) - 1
    if count == 0:
        print(count)
    elif count == 1:
        print(argv[count])
    else:
        while i <= count:
            sum = int(argv[i]) + sum
            i = i + 1
        print(sum)


if __name__ == "__main__":
    infinite()
