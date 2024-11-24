import unittest
from mymath.fibonacci import fibonacci_iterator_show as fibo

N = 10
FIBONACCI_RESULT = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
N_2 = 15
FIBONACCI_RESULT_2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

class FibonacciCase(unittest.TestCase):
    def test_fibonacci_first_case(self):
        self.assertEqual(fibo(N), FIBONACCI_RESULT)  # add assertion here

    def test_fibonacci_second_case(self):
        self.assertEqual(fibo(N_2), FIBONACCI_RESULT_2)  # add assertion here


if __name__ == '__main__':
    unittest.main()