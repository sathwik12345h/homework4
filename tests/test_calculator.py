import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 10, 4, 6),
    ("multiply", 3, 3, 9),
    ("divide", 10, 2, 5),
])
def test_calculator_operations(operation, a, b, expected):
    assert Calculator.execute(operation, a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.execute("divide", 10, 0)

def test_invalid_operation():
    with pytest.raises(ValueError):
        Calculator.execute("invalid", 5, 5)