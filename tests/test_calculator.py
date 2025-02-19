import pytest
from calculator.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(10, 4) == 6

def test_multiply():
    assert Calculator.multiply(3, 3) == 9

def test_divide():
    assert Calculator.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)
