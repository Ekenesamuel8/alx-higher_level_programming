#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_Basic(self):
        e = [2, 3, 6, 9, 1]
        Answer = max_integer(e)
        self.assertEqual(Answer, 9)

    def test_Negetive(self):
        w = [-1, -3, -5, -2]
        Answer = max_integer(w)
        self.assertEqual(Answer, -1)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
            should raise a TypeError exception"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """Test with an empty list: should return None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_module_docstring(self):
        max_integer = __import__('6-max_integer').__doc__
        self.assertTrue(len(max_integer) > 1)
	
    def test_module_docstring(self):
        max_integer = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(max_integer) > 1)


if __name__ == '__main__':
    unittest.main()
