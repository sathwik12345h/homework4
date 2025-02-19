"""Calculator module that provides basic arithmetic operations with history tracking."""
from typing import List, Tuple

class Calculation:
    def __init__(self, operation: str, operand1: float, operand2: float, result: float):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

class Calculator:
    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator._store_calculation("add", a, b, result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator._store_calculation("subtract", a, b, result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator._store_calculation("multiply", a, b, result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator._store_calculation("divide", a, b, result)
        return result

    @classmethod
    def _store_calculation(cls, operation: str, a: float, b: float, result: float) -> None:
        cls.history.append(Calculation(operation, a, b, result))

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
