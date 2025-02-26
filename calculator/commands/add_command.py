from .command import Command

class AddCommand(Command):
    """Command to perform addition."""

    def execute(self, a: float, b: float) -> float:
        return a + b
    