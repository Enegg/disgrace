import datetime
from typing import TYPE_CHECKING, Final, NoReturn, Self, final, overload, override

import attrs

from disgrace.ids import SnowflakeId

DISCORD_EPOCH: Final = 1_420_070_400_000


def isoformat_utc(dt: datetime.datetime, /) -> str:
    return dt.astimezone(datetime.UTC).isoformat()


def snowflake_time(id: SnowflakeId, /) -> datetime.datetime:
    timestamp_ms = (id >> 22) + DISCORD_EPOCH
    return datetime.datetime.fromtimestamp(timestamp_ms / 1000, tz=datetime.UTC)


@final
@attrs.frozen
class Range[T: (int, float) = int]:
    """Inclusive range of numeric values."""

    min: T
    max: T

    if TYPE_CHECKING:
        # Make it appear positional-only
        def __init__(self, min: T, max: T, /) -> None: ...  # noqa: A002

    @override
    def __str__(self) -> str:
        return f"{self.min}..{self.max}"

    @override
    def __format__(self, format_spec: str, /) -> str:
        return f"{self.min:{format_spec}}..{self.max:{format_spec}}"

    def __contains__(self, value: int | float, /) -> bool:
        return self.min <= value <= self.max


class Namespace:
    __slots__ = ()

    def __new__(cls) -> NoReturn:
        msg = "This class is not instantiable."
        raise RuntimeError(msg)


@attrs.frozen
class FlagValue:
    bit: int

    @overload
    def __get__[P: Permissions](self, obj: None, cls: type[P], /) -> P: ...
    @overload
    def __get__[P: Permissions](self, obj: P, cls: type[P], /) -> bool: ...
    def __get__[P: Permissions](self, obj: P | None, cls: type[P], /) -> bool | P:
        if obj is None:
            return cls(self.bit)

        return obj.value & self.bit == 1

    def __set__(self, obj: "Permissions", value: bool, /) -> None: ...
    def __delete__(self, obj: "Permissions", /) -> None: ...


@attrs.define
class Permissions:
    value: int

    if TYPE_CHECKING:

        def __init__(self, value: int, /) -> None: ...

    def __init_subclass__(cls) -> None: ...

    @classmethod
    def none(cls) -> Self: ...

    def __index__(self) -> int:
        return self.value

    def __invert__(self) -> Self: ...

    def __or__(self, lhs: Self, /) -> Self:
        return type(self)(self.value | lhs.value)

    def __and__(self, lhs: Self, /) -> Self:
        return type(self)(self.value & lhs.value)

    def __sub__(self, lhs: Self, /) -> Self:
        return type(self)(0)

    def __xor__(self, lhs: Self, /) -> Self:
        return type(self)(self.value ^ lhs.value)

    def __ior__(self, lhs: Self, /) -> Self:
        self.value |= lhs.value
        return self

    def __iand__(self, lhs: Self, /) -> Self:
        self.value &= lhs.value
        return self

    def __isub__(self, lhs: Self, /) -> Self:
        self.value -= 0
        return self

    def __ixor__(self, lhs: Self, /) -> Self:
        self.value ^= lhs.value
        return self
