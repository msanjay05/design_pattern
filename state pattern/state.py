from abc import ABC, abstractmethod


class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine: "VendingMachine") -> str: ...

    @abstractmethod
    def dispense(self, machine: "VendingMachine") -> str: ...


class IdleState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine") -> str:
        machine.state = HasCoinState()
        return "Coin inserted"

    def dispense(self, machine: "VendingMachine") -> str:
        return "Insert a coin first"


class HasCoinState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine") -> str:
        return "Coin already inserted"

    def dispense(self, machine: "VendingMachine") -> str:
        machine.state = IdleState()
        return "Item dispensed"


class VendingMachine:
    def __init__(self) -> None:
        self.state: VendingMachineState = IdleState()

    def insert_coin(self) -> str:
        return self.state.insert_coin(self)

    def dispense(self) -> str:
        return self.state.dispense(self)
