from abc import ABC, abstractmethod

class ConversionBase(ABC):
    """
    Here Abstract class is for the number conversion operations.
    """

    @abstractmethod
    def convert(self, value):
        pass