from mediator import ChatRoom, User


def main() -> None:
    room = ChatRoom()
    alice = User("Alice", room)
    bob = User("Bob", room)
    room.register(alice)
    room.register(bob)

    alice.send("Hello everyone!")
    print("Bob inbox:", bob.inbox())


if __name__ == "__main__":
    main()
