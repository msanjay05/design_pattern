from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class EditorMemento:
    content: str


class TextEditor:
    def __init__(self) -> None:
        self._content = ""

    def write(self, text: str) -> None:
        self._content = text

    def save(self) -> EditorMemento:
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento) -> None:
        self._content = memento.content

    def show(self) -> str:
        return self._content


class History:
    def __init__(self) -> None:
        self._states: list[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        self._states.append(memento)

    def pop(self) -> Optional[EditorMemento]:
        if not self._states:
            return None
        return self._states.pop()
