#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    list_rev = my_list[::-1]
    for i in range(len(list_rev)):
        print("{:d}".format(list_rev[i]))


if __name__ == "__main__":
    print_reversed_list_integer()
