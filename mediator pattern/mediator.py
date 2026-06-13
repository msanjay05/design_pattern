from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: "Colleague", event: str) -> None: ...


class Colleague(ABC):
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    @abstractmethod
    def send(self, event: str) -> None: ...


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def register(self, user: "User") -> None:
        self._users[user.name] = user

    def notify(self, sender: Colleague, event: str) -> None:
        for name, user in self._users.items():
            if user is not sender:
                user.receive(f"{sender.name}: {event}")


class User(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        super().__init__(mediator)
        self.name = name
        self._messages: list[str] = []

    def send(self, event: str) -> None:
        self._mediator.notify(self, event)

    def receive(self, message: str) -> None:
        self._messages.append(message)

    def inbox(self) -> list[str]:
        return self._messages
