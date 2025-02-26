import abc

class Command(abc.ABC):
    """Abstract base class for commands."""

    @abc.abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass