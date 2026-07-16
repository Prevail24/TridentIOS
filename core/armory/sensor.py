from abc import ABC, abstractmethod


class Sensor(ABC):
    """
    Base class for every Trident IOS sensor.

    Sensors observe.
    Adapters collect/parse.
    Services reason.
    """

    name = "unknown"
    version = "0.1.0"
    produces = []

    @abstractmethod
    def collect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def normalize(self, raw_data):
        raise NotImplementedError

    @abstractmethod
    def emit(self, observations):
        raise NotImplementedError