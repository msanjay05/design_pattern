from facade import Amplifier, DvdPlayer, HomeTheaterFacade, Projector


def main() -> None:
    theater = HomeTheaterFacade(Amplifier(), DvdPlayer(), Projector())
    print(theater.watch_movie("Inception"))


if __name__ == "__main__":
    main()
