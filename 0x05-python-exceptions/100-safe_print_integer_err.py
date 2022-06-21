#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, FloatingPointError, ValueError) as err:
        return False
        sys.stderr.write("Exception: ", err)
