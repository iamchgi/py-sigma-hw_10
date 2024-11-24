import unittest
from mymath.fizz_buzz import fizz_buzz as fb

FIZ_BUZZ_SOURCE_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
FIZ_BUZZ_RESULT_1 = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
                     'FizzBuzz']


class FizBuzzCase(unittest.TestCase):
    def test_normal_data(self):
        self.assertEqual(fb(FIZ_BUZZ_SOURCE_1), FIZ_BUZZ_RESULT_1)

    def test_empty_data(self):
        self.assertEqual(fb([]), [])


if __name__ == '__main__':
    unittest.main()
