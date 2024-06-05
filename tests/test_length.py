import unittest

from length_of_numbers import length_of_number


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(9, length_of_number("semicolon"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
