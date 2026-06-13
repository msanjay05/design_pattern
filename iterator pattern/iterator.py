from abc import ABC, abstractmethod
from collections.abc import Iterator as IteratorABC


class BookCollection:
    def __init__(self, books: list[str]) -> None:
        self._books = books

    def create_iterator(self) -> "BookIterator":
        return BookIterator(self._books)


class BookIterator(IteratorABC):
    def __init__(self, books: list[str]) -> None:
        self._books = books
        self._index = 0

    def __iter__(self) -> "BookIterator":
        return self

    def __next__(self) -> str:
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book
