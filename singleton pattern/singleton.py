"""Singleton: ensures only one instance of a class exists."""


class DatabaseConnection:
    _instance: "DatabaseConnection | None" = None

    def __new__(cls) -> "DatabaseConnection":
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
