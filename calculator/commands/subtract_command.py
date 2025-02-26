from .command import Command

class SubtractCommand(Command):
    """Command to perform subtraction."""

    def execute(self, a: float, b: float) -> float:
        return a - b