#!/usr/bin/python3


def element_at(my_list, idx):
    count = 0
    for i in range(len(my_list)):
        count += 1
    if idx < 0 or idx > count - 1:
        return None
    else:
        return (my_list[idx])


if __name__ == "__main__":
    element_at()
