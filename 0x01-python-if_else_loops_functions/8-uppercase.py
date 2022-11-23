#!/usr/bin/python3
def uppercase(str):
    alp = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in str:
        if i in alp:
            num = ord(i) - 32
            string = string + (chr(num))
        else:
            string = string + i
    print("{}".format(string))
