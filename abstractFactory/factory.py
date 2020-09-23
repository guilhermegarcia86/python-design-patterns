from abstractFactory.invoice import Invoice
from abstractFactory.invoiceIss import InvoiceIss
from abstractFactory.invoiceIcms import InvoiceIcms


class InvoiceFactory:

    def create_invoice(self, name: str) -> Invoice:
        if name == "ICMS":
            return InvoiceIcms()
        else:
            return InvoiceIss()
