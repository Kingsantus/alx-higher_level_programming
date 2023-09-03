#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_import(self):
        try:
            max_integer = __import__('6-max_integer').max_integer
        except ImportError:
            self.fail("Failed to import max_integer from 6-max_integer")

    def test_empty_list(self):
        """Test when the list is empty"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test when the list has a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_integers(self):
        """Test when the list has positive integers"""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_integers(self):
        """Test when the list has negative integers"""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        """Test when the list has both positive and negative integers"""
        result = max_integer([-5, 2, -10, 6, 0])
        self.assertEqual(result, 6)

    def test_duplicate_maximum(self):
        """Test when the list has duplicate maximum values"""
        result = max_integer([1, 2, 3, 4, 5, 5, 5])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
