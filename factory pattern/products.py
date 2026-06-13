"""Product hierarchy for the Factory pattern example."""

from abc import ABC, abstractmethod


class Document(ABC):
    """Abstract product: all export formats implement this interface."""

    @abstractmethod
    def export(self, content: str) -> str:
        """Export content in a specific format."""


class PDFDocument(Document):
    def export(self, content: str) -> str:
        return f"[PDF] {content}"


class WordDocument(Document):
    def export(self, content: str) -> str:
        return f"[Word] {content}"


class HTMLDocument(Document):
    def export(self, content: str) -> str:
        return f"[HTML] {content}"
