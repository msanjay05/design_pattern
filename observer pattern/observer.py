from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> str: ...


class NewsPublisher:
    def __init__(self) -> None:
        self._subscribers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._subscribers.append(observer)

    def publish(self, headline: str) -> list[str]:
        return [observer.update(headline) for observer in self._subscribers]


class EmailSubscriber(Observer):
    def __init__(self, email: str) -> None:
        self._email = email

    def update(self, message: str) -> str:
        return f"Email to {self._email}: {message}"


class SmsSubscriber(Observer):
    def __init__(self, phone: str) -> None:
        self._phone = phone

    def update(self, message: str) -> str:
        return f"SMS to {self._phone}: {message}"
