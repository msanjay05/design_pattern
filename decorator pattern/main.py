from decorators import Milk, SimpleCoffee, Sugar


def main() -> None:
    coffee = Sugar(Milk(SimpleCoffee()))
    print(f"{coffee.description()} -> ${coffee.cost():.2f}")


if __name__ == "__main__":
    main()
