#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        len1 = len(sentence)
        first = sentence[0]
        return (len1, first)


if __name__ == "__main__":
    multiple_returns()
