from adapter.repository import Repository
from factory.invoice import Invoice


def save(repository: Repository, invoice: Invoice) -> None:
    print("Preparing to save")
    repository.save(invoice)


def get_one(repository: Repository, identity: int) -> str:
    print("Preparing to get from storage")
    repository.get_one(identity)
