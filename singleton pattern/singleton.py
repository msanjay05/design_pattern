"""Singleton: ensures only one instance of a class exists."""

import threading


class DatabaseConnection:
    _instance: "DatabaseConnection | None" = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> "DatabaseConnection":
        # First check without lock (optimization)
        if cls._instance is not None:
            return cls._instance
        
        # Acquire lock for thread-safe instance creation
        with cls._lock:
            # Double-check pattern: verify again after acquiring lock
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._connected = False
            return cls._instance

    def connect(self, url: str) -> str:
        if not self._connected:
            self._url = url
            self._connected = True
            return f"Connected to {url}"
        return f"Already connected to {self._url}"

    def query(self, sql: str) -> str:
        return f"Executing on {self._url}: {sql}"
