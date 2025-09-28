import datetime
from typing import TYPE_CHECKING, Final, NoReturn, final, override

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

    def __contains__(self, value: T, /) -> bool:
        return self.min <= value <= self.max


class Namespace:
    __slots__ = ()

    def __new__(cls) -> NoReturn:
        msg = "This class is not instantiable."
        raise RuntimeError(msg)
