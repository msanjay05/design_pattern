from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Image(ABC):
    @abstractmethod
    def display(self) -> str: ...


class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._loaded = self._load()

    def _load(self) -> str:
        return f"Loaded {self._filename} from disk"

    def display(self) -> str:
        return f"Displaying {self._filename}"


class ImageProxy(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real_image: Optional[RealImage] = None

    def display(self) -> str:
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        return self._real_image.display()
