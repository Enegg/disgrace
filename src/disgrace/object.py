import datetime as dt
from collections import abc
from typing import TYPE_CHECKING, Self, SupportsIndex, SupportsInt

import attrs

import disgrace.abc
import disgrace.utils
from disgrace import ids

__all__ = ("Object",)

type SupportsIntCast = SupportsIndex | SupportsInt | str | abc.Buffer


@attrs.frozen
class Object[IdT: ids.SnowflakeId = ids.SnowflakeId]:
    """A generic Discord object."""

    id: IdT = attrs.field(converter=int)

    if TYPE_CHECKING:

        def __init__(self, id: IdT | SupportsIntCast, /) -> None: ...

    @classmethod
    def from_timestamp(cls, timestamp_ms: int | dt.datetime, /) -> Self:
        if isinstance(timestamp_ms, dt.datetime):
            timestamp_ms = int(timestamp_ms.timestamp() * 1000)

        return cls(timestamp_ms - disgrace.utils.DISCORD_EPOCH << 22)

    def created_after(self, snowflake: disgrace.abc.Snowflake, /) -> bool:
        return self.id >> 22 > snowflake.id >> 22

    def created_before(self, snowflake: disgrace.abc.Snowflake, /) -> bool:
        return self.id >> 22 < snowflake.id >> 22
