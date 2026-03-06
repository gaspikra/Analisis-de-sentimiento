from abc import ABC, abstractmethod


class ICleanDataFilter(ABC):
    @abstractmethod
    def process(self, data):
        pass