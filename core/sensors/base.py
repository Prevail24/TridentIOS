from abc import ABC, abstractmethod


class Sensor(ABC):
    """
    Base class for every Trident sensor.
    """

    name = "unknown"

    @abstractmethod
    def collect(self):
        """Run the external tool."""
        raise NotImplementedError

    @abstractmethod
    def emit(self):
        """Return canonical observations."""
        raise NotImplementedError