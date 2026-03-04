from abc import ABC, abstractmethod


class ICleanDataStrategy(ABC):
    @abstractmethod
    def clean_data(self, dataFrame):
        pass