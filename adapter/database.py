from adapter.repository import Repository
from factory.invoice import Invoice


class Database(Repository):

    def save(self, invoice: Invoice):
        print(f"Saving with class {type(invoice).__name__}")

    def get_one(self, identity: int) -> str:
        return f'Database#get_one'
