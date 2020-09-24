from adapter.database import Database
from adapter.file_system_storage import FileSystemStorage
from adapter.adapter import save, get_one
from factory.factory import InvoiceFactory


invoice_icms = "ICMS"
invoice_iss = "ISS"

invoice = InvoiceFactory.create_invoice(invoice_icms)

print(invoice.calculate_rate())

repository = Database()

save(repository, invoice)
get_one(repository, 1)


invoice = InvoiceFactory.create_invoice(invoice_iss)

print(invoice.calculate_rate())

repository = FileSystemStorage()

save(repository, invoice)
get_one(repository, 1)
