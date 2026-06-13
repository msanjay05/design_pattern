from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: "ShapeVisitor") -> str: ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: "ShapeVisitor") -> str:
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def accept(self, visitor: "ShapeVisitor") -> str:
        return visitor.visit_rectangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle) -> str: ...

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> str: ...


class AreaVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        area = 3.14 * circle.radius**2
        return f"Circle area: {area:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        area = rectangle.width * rectangle.height
        return f"Rectangle area: {area:.2f}"


class ExportVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        return f'{{"type": "circle", "radius": {circle.radius}}}'

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return (
            f'{{"type": "rectangle", '
            f'"width": {rectangle.width}, "height": {rectangle.height}}}'
        )
