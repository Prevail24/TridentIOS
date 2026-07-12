from abc import ABC, abstractmethod


class ToolAdapter(ABC):
    """
    Base interface for every reconnaissance tool.

    Every adapter is responsible for:

    - Executing the tool
    - Producing evidence
    - Emitting observations
    """

    @abstractmethod
    def execute(self):
        raise NotImplementedError