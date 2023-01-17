#!/usr/bin/python3
"""unitest for testing rectangle"""

import unittest
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Rectangle(unittest.TestCase):
    
#area() function test
    def test_area(self):
        self.assertEqual(Rectangle(5, 6).area(), 30)
    def test_area(self):
        self.assertEqual(Rectangle(5, 5).area(), 25)


#str() function
    def test_str_str_method(self):
        expected = "[Rectangle] (3) 6/9 - 5/2"
        self.assertEqual(Rectangle(5, 2, 6, 9, 89).__str__(), expected)

    def test_str_str(self):
        expected = "[Rectangle] (3) 0/0 - 3/4"
        self.assertEqual(str(Rectangle(3, 4)), expected)

    def test_str_str_method_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).__str__(42)
#dictonary
    def test_to_dictionary_basic(self):
        r = Rectangle(5, 4, 4, 2, 3)
        expected = {'width': 5, 'height': 4, 'x': 4, 'y': 2, 'id': 4}
        self.assertDictEqual(r.to_dictionary(), expected)

    def test_to_dictionary_basic_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 20, 2, 34).to_dictionary(34)


if __name__ == "__main__":
    unittest.main()
