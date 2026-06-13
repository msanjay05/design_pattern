"""Demonstrates Simple Factory and Factory Method patterns."""

from factory_method import HTMLFactory, PDFFactory, WordFactory
from simple_factory import DocumentSimpleFactory


def demo_simple_factory() -> None:
    print("=== Simple Factory ===")
    for doc_type in ("pdf", "word", "html","text"):
        document = DocumentSimpleFactory.create(doc_type)
        if document:
            print(document.export(f"Report exported as {doc_type.upper()}"))
        else:
            print(f"Unsupported document type: {doc_type.upper()}")


def demo_factory_method() -> None:
    print("\n=== Factory Method ===")
    factories = (PDFFactory(), WordFactory(), HTMLFactory())
    for factory in factories:
        print(factory.export_report("Quarterly sales summary"))


if __name__ == "__main__":
    demo_simple_factory()
    demo_factory_method()
