from dataclasses import dataclass, field


@dataclass
class Pizza:
    size: str = ""
    crust: str = ""
    toppings: list[str] = field(default_factory=list)

    def describe(self) -> str:
        toppings = ", ".join(self.toppings) or "plain"
        return f"{self.size} {self.crust} pizza with {toppings}"
