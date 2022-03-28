import dataclasses
from arcade import Texture
from typing import Callable
from Setup import vector


@dataclasses.dataclass(unsafe_hash=True)
class Interactable:
    id: str = dataclasses.field(hash=True)
    sprite: str = dataclasses.field(hash=True)
    bounds: tuple[vector.Vector, vector.Vector] = dataclasses.field(hash=True)
    on_interact: Callable = dataclasses.field(hash=False)

    @property
    def center(self):
        return vector.Vector(((self.bounds[0].x + self.bounds[1].x) / 2), ((self.bounds[0].y + self.bounds[1].y) / 2))

    @property
    def size(self):
        return vector.Vector(abs(self.bounds[0].x - self.bounds[1].x), abs(self.bounds[0].y - self.bounds[1].y))

