from .command import Command

class MultiplyCommand(Command):
    """Command to perform multiplication."""

    def execute(self, a: float, b: float) -> float:
        return a * b