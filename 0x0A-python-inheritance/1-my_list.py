#!/usr/bin/python3


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        """ sorts a list"""

        print(sorted(self))
