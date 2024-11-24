import unittest
from my_math.fibonacci import fibonacci_iterator as fibo

N = 10
FIBONACCI_RESULT = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
N_2 = 15
FIBONACCI_RESULT_2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

class FibonacciCases(unittest.TestCase):
    def test_fibonacci_first_case(self):
        self.assertEqual(fibo(N), FIBONACCI_RESULT)

    def test_fibonacci_second_case(self):
        self.assertEqual(fibo(N_2), FIBONACCI_RESULT_2)

if __name__ == '__main__':
    unittest.main()
