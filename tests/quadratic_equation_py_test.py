import pytest

from mymath.quadratic_equation import square_eq_solver


def test_one_two_three():
    result = square_eq_solver(1,2,3)
    assert result == []
    result = square_eq_solver(3, -2, -3)
    assert result == [1.3874258867227933, -0.7207592200561265]