from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_factory.invoice import Invoice


class AbstractFactory(ABC):

    @abstractmethod
    def create_invoice(self, name: str) -> Invoice:
        pass
