from product import Pizza


class PizzaBuilder:
    def __init__(self) -> None:
        self._pizza = Pizza()

    def size(self, value: str) -> "PizzaBuilder":
        self._pizza.size = value
        return self

    def crust(self, value: str) -> "PizzaBuilder":
        self._pizza.crust = value
        return self

    def add_topping(self, topping: str) -> "PizzaBuilder":
        self._pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        return self._pizza
