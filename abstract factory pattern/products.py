from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Button]"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows Checkbox]"


class MacButton(Button):
    def render(self) -> str:
        return "[Mac Button]"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "[Mac Checkbox]"
