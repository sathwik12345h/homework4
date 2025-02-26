from .command import Command

class DivideCommand(Command):
    """Command to perform division."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b