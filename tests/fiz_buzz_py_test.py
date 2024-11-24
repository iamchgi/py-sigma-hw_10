import pytest
from my_math.fizz_buzz import fizz_buzz as fb

FIZ_BUZZ_SOURCE_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
FIZ_BUZZ_RESULT_1 = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
                     'FizzBuzz']


def test_normal_data():
    result = fb(FIZ_BUZZ_SOURCE_1)
    assert result == FIZ_BUZZ_RESULT_1


def test_empty_data():
    result = fb([])
    assert result == []


if __name__ == '__main__':
    pass
