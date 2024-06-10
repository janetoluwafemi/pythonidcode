import unittest

from evenOrOdd import evenOrOddCheck
class MyTestCase(unittest.TestCase):
    def test_even(self):
        self.assertTrue(True, 2)  # add assertion here

    def test_odd(self):
        self.assertTrue(True,3)

if __name__ == '__main__':
    unittest.main()
