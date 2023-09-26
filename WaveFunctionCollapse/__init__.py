import abc


class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    @abc.abstractmethod
    def draw(self):
        raise NotImplemented()


class CellUp(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def draw(self):
        pass


class WaveFunctionCollapse:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size
        self.cells: list[Cell] = []
