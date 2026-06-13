from abc import ABC, abstractmethod

from devices import Device


class RemoteControl(ABC):
    def __init__(self, device: Device) -> None:
        self._device = device

    @abstractmethod
    def toggle(self) -> str: ...


class BasicRemote(RemoteControl):
    def toggle(self) -> str:
        if self._device.is_enabled():
            return self._device.disable()
        return self._device.enable()


class AdvancedRemote(RemoteControl):
    def toggle(self) -> str:
        action = self._device.disable() if self._device.is_enabled() else self._device.enable()
        return f"[Advanced] {action}"
