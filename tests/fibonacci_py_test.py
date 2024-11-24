import pytest
from my_math import fibo

N = 10
FIBONACCI_RESULT = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
N_2 = 15
FIBONACCI_RESULT_2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


def test_fibonacci_first_case():
    result = fibo(N)
    assert result == FIBONACCI_RESULT


def test_fibonacci_second_case():
    result = fibo(N_2)
    assert result == FIBONACCI_RESULT_2

if __name__ == '__main__':
    pass