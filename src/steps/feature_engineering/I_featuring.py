from abc import ABC, abstractmethod


class IFeaturing(ABC):
    @abstractmethod
    def process(self, data):
        pass