#!/usr/bin/env python

"""Tests for `geodemora` package."""


import unittest

from geodemora import utils


class TestUtils(unittest.TestCase):
    """Tests for `utils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown\n")

    def test_random_string(self):
        """Tear down test fixtures, if any."""
        print("test_random_string")
        self.assertEqual(len(utils.random_string(3)), 3)

    def test_add(self):
        """Test something."""
        print("test_add")
        self.assertEqual(utils.add(-1, 1), 0)
        self.assertEqual(utils.add(10, 5), 15)

    def test_subatract(self):
        print("test_subtract")
        self.assertEqual(utils.subtract(10, 5), 5)
        self.assertEqual(utils.subtract(-1, -1), 0)
        self.assertEqual(utils.subtract(-2, 3), -5)

    def test_multiply(self):
        print("test_multiply")
        self.assertEqual(utils.multiply(2, 5), 10)
        self.assertEqual(utils.multiply(1, 0), 0)
        self.assertEqual(utils.multiply(3, -5), -15)

if __name__ == '__main__':
    unittest.main()

