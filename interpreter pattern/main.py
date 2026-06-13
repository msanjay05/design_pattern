from expressions import Add, Number, Subtract, Variable


def main() -> None:
    # Interprets: (x + y) - 3
    expression = Subtract(Add(Variable("x"), Variable("y")), Number(3))
    context = {"x": 10, "y": 5}

    print(f"Result: {expression.interpret(context)}")


if __name__ == "__main__":
    main()
