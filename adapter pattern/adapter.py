class LegacyPaymentGateway:
    def make_payment(self, amount: float, currency: str) -> str:
        return f"Legacy charge: {amount} {currency}"


class PaymentProcessor:
    def pay(self, amount: float) -> str: ...


class LegacyPaymentAdapter(PaymentProcessor):
    def __init__(self, legacy: LegacyPaymentGateway) -> None:
        self._legacy = legacy

    def pay(self, amount: float) -> str:
        return self._legacy.make_payment(amount, "USD")


class StripePaymentProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Stripe charge: ${amount:.2f}"
