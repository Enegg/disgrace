import colorsys
import random
from typing import Protocol, Self

import attrs

__all__ = ("Color",)


class RandomGen(Protocol):
    def random(self) -> float: ...


@attrs.frozen
class Color:
    """A Discord color value."""

    value: int
    """The raw color value."""

    def __index__(self) -> int:
        return self.value

    @property
    def red(self) -> int:
        return (self.value >> 16) & 0xFF

    @property
    def green(self) -> int:
        return (self.value >> 8) & 0xFF

    @property
    def blue(self) -> int:
        return self.value & 0xFF

    def to_rgb(self) -> tuple[int, int, int]:
        return (self.red, self.green, self.blue)

    @classmethod
    def from_rgb(cls, red: int, green: int, blue: int) -> Self:
        return cls((red << 16) + (green << 8) + blue)

    def to_hsv(self) -> tuple[float, float, float]:
        return colorsys.rgb_to_hsv(self.red / 255, self.green / 255, self.blue / 255)

    @classmethod
    def from_hsv(cls, hue: float, saturation: float, value: float) -> Self:
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        return cls.from_rgb(int(r * 255), int(g * 255), int(b * 255))

    @classmethod
    def from_hex(cls, value: str, /) -> Self:
        """Create a `Color` from a `#rrggbb` string."""
        return cls(int(value.removeprefix("#").removeprefix("0x"), base=16))

    @classmethod
    def random_hue(cls, *, gen: RandomGen = random) -> Self:
        """Create a `Color` with random hue."""
        return cls.from_hsv(gen.random(), 1, 1)
