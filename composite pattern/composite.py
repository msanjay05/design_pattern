from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: int = 0) -> str: ...

    @abstractmethod
    def size(self) -> int: ...


class File(FileSystemComponent):
    def __init__(self, name: str, kilobytes: int) -> None:
        self._name = name
        self._kilobytes = kilobytes

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}{self._name} ({self._kilobytes} KB)"

    def size(self) -> int:
        return self._kilobytes


class Folder(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self._name = name
        self._children: list[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        lines = [f"{prefix}{self._name}/"]
        for child in self._children:
            lines.append(child.display(indent + 1))
        return "\n".join(lines)

    def size(self) -> int:
        return sum(child.size() for child in self._children)
