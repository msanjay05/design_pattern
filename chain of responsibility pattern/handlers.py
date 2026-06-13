from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    def __init__(self) -> None:
        self._next: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]: ...

    def _pass_to_next(self, request: str) -> Optional[str]:
        if self._next:
            return self._next.handle(request)
        return None


class AuthHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if "token" not in request:
            return "AuthHandler: missing token"
        return self._pass_to_next(request)


class RateLimitHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if "burst" in request:
            return "RateLimitHandler: too many requests"
        return self._pass_to_next(request)


class BusinessHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        return f"BusinessHandler: processed '{request}'"
