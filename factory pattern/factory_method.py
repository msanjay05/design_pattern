"""Factory Method: subclasses decide which concrete product to instantiate."""

from abc import ABC, abstractmethod

from products import Document, HTMLDocument, PDFDocument, WordDocument


class DocumentFactory(ABC):
    """Creator declares the factory method; concrete factories provide products."""

    @abstractmethod
    def create_document(self) -> Document:
        """Factory method."""

    def export_report(self, content: str) -> str:
        """Uses the product without knowing its concrete class."""
        document = self.create_document()
        return document.export(content)


class PDFFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()


class WordFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()


class HTMLFactory(DocumentFactory):
    def create_document(self) -> Document:
        return HTMLDocument()
