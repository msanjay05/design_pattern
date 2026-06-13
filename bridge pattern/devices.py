from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool: ...

    @abstractmethod
    def enable(self) -> str: ...

    @abstractmethod
    def disable(self) -> str: ...


class TV(Device):
    def __init__(self) -> None:
        self._on = False

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> str:
        self._on = True
        return "TV enabled"

    def disable(self) -> str:
        self._on = False
        return "TV disabled"


class Radio(Device):
    def __init__(self) -> None:
        self._on = False

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> str:
        self._on = True
        return "Radio enabled"

    def disable(self) -> str:
        self._on = False
        return "Radio disabled"
