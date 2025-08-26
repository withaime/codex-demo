import pytest
from calculator import calculate


def test_addition():
    assert calculate(1, 2, '+') == 3


def test_subtraction():
    assert calculate(5, 3, '-') == 2


def test_multiplication():
    assert calculate(4, 3, '*') == 12


def test_division():
    assert calculate(10, 2, '/') == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, '/')


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(1, 2, '%')
