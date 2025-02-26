from typing import Dict, Type
from .commands.add_command import AddCommand
from .commands.subtract_command import SubtractCommand
from .commands.multiply_command import MultiplyCommand
from .commands.divide_command import DivideCommand
from .commands.command import Command

class Calculator:
    """Calculator class using the Command Pattern."""

    commands: Dict[str, Type[Command]] = {
        "add": AddCommand(),
        "subtract": SubtractCommand(),
        "multiply": MultiplyCommand(),
        "divide": DivideCommand(),
    }

    @classmethod
    def execute(cls, operation: str, a: float, b: float) -> float:
        """Executes a command based on the operation name."""
        command = cls.commands.get(operation)
        if not command:
            raise ValueError(f"Unknown operation: {operation}")
        return command.execute(a, b)