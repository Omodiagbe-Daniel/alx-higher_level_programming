#!/usr/bin/python3
from sys import argv


def list_arg():
    i = 1
    len_arg = len(argv) - 1
    if len_arg < 1:
        print(f"{len_arg} argument.")
    elif len_arg == 1:
        print(f"{len_arg} argument:")
        print(f"{len_arg}: {argv[len_arg]}")
    else:
        print(f"{len_arg} arguments:")
        while i <= len_arg:
            print(f"{i}: {argv[i]}")
            i = i + 1


if __name__ == "__main__":
    list_arg()
