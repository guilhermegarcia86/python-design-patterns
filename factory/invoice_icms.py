from factory.invoice import Invoice


class InvoiceIcms(Invoice):
    def calculate_rate(self) -> str:
        return "Processing ICMS tax"
