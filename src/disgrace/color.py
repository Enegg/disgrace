import colorsys
import random
from typing import ClassVar, Self

import attrs

__all__ = ("Color",)


@attrs.frozen
class Color:
    """A Discord color value."""

    none: ClassVar[Self]
    """Special value denoting lack of color."""
    value: int

    @property
    def red(self) -> int:
        return self.value >> 16 & 0xFF

    @property
    def green(self) -> int:
        return (self.value >> 8) & 0xFF

    @property
    def blue(self) -> int:
        return self.value & 0xFF

    def __bool__(self) -> bool:
        return bool(self.value)

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
    def random(cls, *, seed: int | float | str | bytes | bytearray | None = None) -> Self:
        """Create a `Color` with random hue."""
        rand = random if seed is None else random.Random(seed)
        return cls.from_hsv(rand.random(), 1, 1)


Color.none = Color(0)
