#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tup = 0
    tupl = 0
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 > 2 or len2 > 2:
        tuple_a = tuple_a[0:2]
        tuple_b = tuple_a[0:2]
    elif len1 == 1:
        tuple_a = tuple_a + (0,)
    elif len1 == 0:
        tuple_a = tuple_a + (0, 0)
    if len2 == 1:
        tuple_b = tuple_b + (0,)
    elif len2 == 0:
        tuple_b = tuple_b + (0, 0)
    for i in range(len(tuple_a)):
        for j in range(len(tuple_b)):
            if i == j and i == 0:
                tupl = tuple_a[i] + tuple_b[i] + tupl
            elif i == j and i == 1:
                tup = tuple_a[i] + tuple_b[i] + tup
    tuple = (tupl, tup)
    return tuple


if __name__ == "__main__":
    add_tuple()
