from abstract_factory.invoice import Invoice
from abstract_factory.invoice_iss import InvoiceIss
from abstract_factory.invoice_icms import InvoiceIcms


class InvoiceFactory:

    @staticmethod
    def create_invoice(name: str) -> Invoice:
        if name == "ICMS":
            return InvoiceIcms()
        else:
            return InvoiceIss()
