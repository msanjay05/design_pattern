from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict[str, int]) -> int: ...


class Number(Expression):
    def __init__(self, value: int) -> None:
        self._value = value

    def interpret(self, context: dict[str, int]) -> int:
        return self._value


class Variable(Expression):
    def __init__(self, name: str) -> None:
        self._name = name

    def interpret(self, context: dict[str, int]) -> int:
        return context[self._name]


class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) + self._right.interpret(context)


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) - self._right.interpret(context)
