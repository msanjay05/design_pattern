from visitor import AreaVisitor, Circle, ExportVisitor, Rectangle


def main() -> None:
    shapes = [Circle(3), Rectangle(4, 5)]
    area_visitor = AreaVisitor()
    export_visitor = ExportVisitor()

    for shape in shapes:
        print(shape.accept(area_visitor))
        print(shape.accept(export_visitor))


if __name__ == "__main__":
    main()
