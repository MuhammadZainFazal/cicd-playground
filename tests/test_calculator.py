import pytest

from app.calculator import add, divide, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8


def test_power_negative_exponent():
    assert power(2, -1) == 0.5


def test_power_zero_to_negative():
    with pytest.raises(ValueError):
        power(0, -1)


def test_power_complex_result():
    with pytest.raises(ValueError):
        power(-8, 0.5)


def test_power_overflow():
    with pytest.raises(ValueError):
        power(10.0, 100000)
    assert False
