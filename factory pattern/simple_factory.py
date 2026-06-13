"""Simple Factory: one place creates objects based on a type key."""

from products import Document, HTMLDocument, PDFDocument, WordDocument


class DocumentSimpleFactory:
    """Creates document instances without exposing concrete classes to clients."""

    _registry: dict[str, type[Document]] = {
        "pdf": PDFDocument,
        "word": WordDocument,
        "html": HTMLDocument,
    }

    @classmethod
    def create(cls, document_type: str) -> Document:
        key = document_type.lower()
        try:
            return cls._registry[key]()
        except KeyError as exc:
            supported = ", ".join(sorted(cls._registry))
            return None
            raise ValueError(
                f"Unsupported document type: {document_type!r}. "
                f"Supported types: {supported}."
            ) from exc
