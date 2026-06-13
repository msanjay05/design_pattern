class TreeType:
    """Intrinsic state shared across many tree objects."""

    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> str:
        return f"{self.name} ({self.color}, {self.texture}) at ({x}, {y})"


class TreeFactory:
    _pool: dict[tuple[str, str, str], TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._pool:
            cls._pool[key] = TreeType(name, color, texture)
        return cls._pool[key]

    @classmethod
    def pool_size(cls) -> int:
        return len(cls._pool)


class Tree:
    """Extrinsic state: position varies per instance."""

    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self._x = x
        self._y = y
        self._type = tree_type

    def draw(self) -> str:
        return self._type.draw(self._x, self._y)
