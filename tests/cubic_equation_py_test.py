import pytest

from mymath.cubic_equation import cubic_eq_solver


def test_1():
    result = cubic_eq_solver(1,1,1, 1)
    assert result == []
