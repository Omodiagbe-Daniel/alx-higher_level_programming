#!/usr/bin/python3
"""unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """testing for max integer"""

    def test_ordered_list(self):
        """testing ordered list"""
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)

    def test_unordered_list(self):
        """testing un-ordered list"""
        list2 = [3, 6, 1, 4]
        self.assertEqual(max_integer(list2), 6)

    def test_single_number(self):
        """testing if only one int is in the list"""
        list3 = [6]
        self.assertEqual(max_integer(list3), 6)

    def test_empty_list(self):
        """testing an empty list"""
        list4 = []
        self.assertEqual(max_integer(list4), None)

    def test_float(self):
        """testing max float"""
        list6 = [2.5, 7.9, 6, 4]
        self.assertEqual(max_integer(list6), 7.9)


if __name__ == "__main__":
    unittest.main()
