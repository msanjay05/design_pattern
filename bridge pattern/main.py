from devices import Radio, TV
from remotes import AdvancedRemote, BasicRemote


def main() -> None:
    tv_remote = BasicRemote(TV())
    radio_remote = AdvancedRemote(Radio())

    print(tv_remote.toggle())
    print(tv_remote.toggle())
    print(radio_remote.toggle())


if __name__ == "__main__":
    main()
