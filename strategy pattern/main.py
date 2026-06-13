from strategy import Checkout, CreditCardPayment, PayPalPayment


def main() -> None:
    checkout = Checkout(CreditCardPayment())
    print(checkout.complete(120.0))

    checkout.set_strategy(PayPalPayment())
    print(checkout.complete(45.5))


if __name__ == "__main__":
    main()
