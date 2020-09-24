from adapter.database import Database
from adapter.file_system_storage import FileSystemStorage
from adapter.adapter import save, get_one
from factory.factory import InvoiceFactory
from observer.email_observer import EmailObserver
from observer.email_subject import EmailSubject

invoice_icms = "ICMS"
invoice_iss = "ISS"

subject = EmailSubject()
fiscal = EmailObserver("dept_fiscal")
financial = EmailObserver("dept_financial")
subject.subscribe(fiscal)
subject.subscribe(financial)

invoice = InvoiceFactory.create_invoice(invoice_icms)

print(invoice.calculate_rate())

repository = Database()

save(repository, invoice)

subject.add_email(type(invoice).__name__)

get_one(repository, 1)


invoice = InvoiceFactory.create_invoice(invoice_iss)

print(invoice.calculate_rate())

repository = FileSystemStorage()

save(repository, invoice)

subject.add_email(type(invoice).__name__)

get_one(repository, 1)
