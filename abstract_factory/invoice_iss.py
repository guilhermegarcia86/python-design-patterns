from abstract_factory.invoice import Invoice


class InvoiceIss(Invoice):
    def calculate_rate(self) -> str:
        return "Processing Iss tax"
