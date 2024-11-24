import pytest

from my_math.quadratic_equation import square_eq_solver


def test_no_root():
    result = square_eq_solver(1,2,3)
    assert result == []

def test_two_root():
    result = square_eq_solver(3, -2, -3)
    assert result == [1.3874258867227933, -0.7207592200561265]

def test_single_root():
    result = square_eq_solver(10, 0, 0)
    assert len(result) == 1
    assert result == [0]

def test_multiple_root():
    result = square_eq_solver(2, 5, -3)
    assert len(result) == 2
    assert result == [0.5, -3]

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        square_eq_solver(0, 0, 0)
