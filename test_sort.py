# test_sort.py
"""
Purpose: The assignment requests we write tests to demonstrate a testing process
"""

import unittest
from main import sort_integers, sort_strings

class TestSortingFunctions(unittest.TestCase):
    def test_sort_integers_ascending(self):
        input_list = [3, 1, 2, 0, -1]
        expected = [-1, 0, 1, 2, 3]
        self.assertEqual(sort_integers(input_list), expected)
    
    def test_sort_integers_descending(self):
        input_list = [3, 1, 2]
        expected = [3, 2, 1]
        self.assertEqual(sort_integers(input_list, descending=True), expected)

    def test_sort_strings_alphabetical(self):
        input_list = ["banana", "apple", "cherry"]
        expected = ["apple", "banana", "cherry"]
        self.assertEqual(sort_strings(input_list), expected)
    
    def test_sort_string_reverse_alphabetical(self):
        input_list = ["banana", "apple", "cherry"]
        expected = ["cherry", "banana", "apple"]
        self.assertEqual(sort_strings(input_list, reverse=True), expected)

if __name__ == "__main__":
    unittest.main()