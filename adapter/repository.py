from abc import ABC
from factory.invoice import Invoice


class Repository(ABC):
    def save(self, invoice: Invoice):
        pass

    def get_one(self, identity: int) -> str:
        pass
