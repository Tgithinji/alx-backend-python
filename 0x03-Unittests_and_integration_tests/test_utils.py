#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, output):
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ('a',), KeyError, 'a'),
        ({'a': 1}, ('a', 'b'), KeyError, 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, output):
        with self.assertRaises(output):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
