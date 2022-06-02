#!/usr/bin/python3
import hidden_4


def hidden():
    file = dir(hidden_4)
    count = len(file)
    for i in range(count):
        if file[i][0:2] != "__":
            print(file[i])


if __name__ == "__main__":
    hidden()
