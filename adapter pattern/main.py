from adapter import (
    LegacyPaymentAdapter,
    LegacyPaymentGateway,
    PaymentProcessor,
    StripePaymentProcessor,
)


def checkout(processor: PaymentProcessor, amount: float) -> None:
    print(processor.pay(amount))


def main() -> None:
    print("=== Legacy (via Adapter) ===")
    legacy_processor = LegacyPaymentAdapter(LegacyPaymentGateway())
    checkout(legacy_processor, 49.99)

    print("\n=== New Processor (direct) ===")
    stripe_processor = StripePaymentProcessor()
    checkout(stripe_processor, 49.99)


if __name__ == "__main__":
    main()
