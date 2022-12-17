#!/usr/bin/python3
"""matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """performs matrix multiplication"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for ls in m_a:
        for ele in ls:
            if type(ele) not in (int, float):
                raise (TypeError
                       ("m_a should contain only integers or floats"))
    for ele in m_b:
        for el in ele:
            if type(el) not in (int, float):
                raise (TypeError
                       ("m_b should contain only integers or floats"))

    len_m_a = len(m_a[0])
    for elem in m_a:
        if len(elem) != len_m_a:
            raise (TypeError
                   ("each row of m_a must be of the same size"))
    len_m_b = len(m_b[0])
    for ele in m_b:
        if len(ele) != len_m_a:
            raise (TypeError
                   ("each row of m_b must be of the same size"))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
