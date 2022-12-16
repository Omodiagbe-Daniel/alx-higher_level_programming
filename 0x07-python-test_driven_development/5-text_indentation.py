#!/usr/bin/python3
"""Text indention module"""


def text_indentation(text):
    """prints a text with 2 new lines after
        each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = ""
    str_list = []
    for i in text:
        string = string + i
        if i == "." or i == "?" or i == ":":
            str_list.append(string)
            string = ""
    str_list.append(string)
    for strg in range(len(str_list)):
        if strg < len(str_list) - 1:
            print(str_list[strg].strip())
            print()
        else:
            print(str_list[strg].strip(), end='')
