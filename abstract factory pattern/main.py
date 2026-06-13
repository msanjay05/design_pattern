from factories import MacUIFactory, WindowsUIFactory


def render_form(factory_name: str, factory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(f"{factory_name}: {button.render()}, {checkbox.render()}")


def main() -> None:
    render_form("Windows", WindowsUIFactory())
    render_form("Mac", MacUIFactory())


if __name__ == "__main__":
    main()
