import copy
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Document(ABC):
    @abstractmethod
    def clone(self) -> "Document": ...

    @abstractmethod
    def show(self) -> str: ...


@dataclass
class Report(Document):
    title: str
    sections: list[str] = field(default_factory=list)

    def clone(self) -> "Report":
        return copy.deepcopy(self)

    def show(self) -> str:
        body = " | ".join(self.sections)
        return f"{self.title}: {body}"
