from factory.factory import InvoiceFactory

invoice_icms = "ICMS"
invoice_iss = "ISS"

invoice = InvoiceFactory.create_invoice(invoice_icms)

print(invoice.calculate_rate())

invoice = InvoiceFactory.create_invoice(invoice_iss)

print(invoice.calculate_rate())