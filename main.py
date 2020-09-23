from abstract_factory.factory import InvoiceFactory

invoice_icms = "ICMS"

invoice = InvoiceFactory.create_invoice(invoice_icms)

print(invoice)
