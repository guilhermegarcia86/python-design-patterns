from abc import ABC, abstractmethod


class Invoice(ABC):

    @abstractmethod
    def calculate_rate(self) -> str:
        pass
