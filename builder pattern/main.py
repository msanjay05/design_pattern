from builder import PizzaBuilder


def main() -> None:
    pizza = (
        PizzaBuilder()
        .size("Large")
        .crust("thin")
        .add_topping("mozzarella")
        .add_topping("basil")
        .build()
    )
    print(pizza.describe())


if __name__ == "__main__":
    main()
