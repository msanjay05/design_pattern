from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> str: ...

    @abstractmethod
    def undo(self) -> str: ...


class Light:
    def on(self) -> str:
        return "Light is ON"

    def off(self) -> str:
        return "Light is OFF"


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> str:
        return self._light.on()

    def undo(self) -> str:
        return self._light.off()


class RemoteControl:
    def __init__(self) -> None:
        self._history: list[Command] = []

    def press(self, command: Command) -> str:
        self._history.append(command)
        return command.execute()

    def undo_last(self) -> str:
        if not self._history:
            return "Nothing to undo"
        return self._history.pop().undo()
