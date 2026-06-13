class Amplifier:
    def on(self) -> str:
        return "Amplifier on"


class DvdPlayer:
    def play(self, movie: str) -> str:
        return f"Playing {movie}"


class Projector:
    def on(self) -> str:
        return "Projector on"


class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, dvd: DvdPlayer, projector: Projector) -> None:
        self._amp = amp
        self._dvd = dvd
        self._projector = projector

    def watch_movie(self, movie: str) -> str:
        steps = [
            self._amp.on(),
            self._projector.on(),
            self._dvd.play(movie),
        ]
        return " -> ".join(steps)
