from command import Light, LightOnCommand, RemoteControl


def main() -> None:
    remote = RemoteControl()
    print(remote.press(LightOnCommand(Light())))
    print(remote.undo_last())


if __name__ == "__main__":
    main()
