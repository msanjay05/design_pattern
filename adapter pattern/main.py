from adapter import LegacyPaymentAdapter, LegacyPaymentGateway


def main() -> None:
    processor = LegacyPaymentAdapter(LegacyPaymentGateway())
    print(processor.pay(49.99))


if __name__ == "__main__":
    main()
