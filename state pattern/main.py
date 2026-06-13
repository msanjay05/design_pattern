from state import VendingMachine


def main() -> None:
    machine = VendingMachine()
    print(machine.dispense())
    print(machine.insert_coin())
    print(machine.dispense())


if __name__ == "__main__":
    main()
