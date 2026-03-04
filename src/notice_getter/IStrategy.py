from abc import ABC, abstractmethod

class IDataStrategy(ABC):

    @abstractmethod
    def obtain_data(self,ticker, start, end, **kwargs):
        pass
    