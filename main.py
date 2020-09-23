from abstractFactory.abstractFactory import AbstractFactory
from abstractFactory.factory import InvoiceFactory

invoiceIcms = "ICMS"
invoiceIss = "ISS"

invoice = InvoiceFactory.create_invoice(invoiceIcms)

print(invoice)