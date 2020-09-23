from factory.invoice import Invoice
from factory.invoice_iss import InvoiceIss
from factory.invoice_icms import InvoiceIcms


class InvoiceFactory:

    @staticmethod
    def create_invoice(name: str) -> Invoice:
        if name == "ICMS":
            return InvoiceIcms()
        else:
            return InvoiceIss()
