import datetime
from typing import TYPE_CHECKING, Self, SupportsInt

import attrs

import disgrace.abc
import disgrace.utils
from disgrace import ids

__all__ = ("Object",)

type SupportsIntCast = SupportsInt | str | bytes | bytearray


@attrs.frozen
class Object[IdT: ids.SnowflakeId = ids.SnowflakeId]:
    """A generic Discord object."""

    id: IdT = attrs.field(converter=int)

    __eq__ = disgrace.abc.Snowflake[IdT].__eq__
    __hash__ = disgrace.abc.Snowflake[IdT].__hash__

    if TYPE_CHECKING:

        def __init__(self, id: IdT | SupportsIntCast, /) -> None: ...

    @classmethod
    def from_timestamp(cls, ts_ms: int | datetime.datetime, /) -> Self:
        if isinstance(ts_ms, datetime.datetime):
            ts_ms = int(ts_ms.timestamp() * 1000)

        return cls(ts_ms - disgrace.utils.DISCORD_EPOCH << 22)

    def created_after(self, snowflake: disgrace.abc.HasId[ids.SnowflakeId], /) -> bool:
        return self.id >> 22 > snowflake.id >> 22

    def created_before(self, snowflake: disgrace.abc.HasId[ids.SnowflakeId], /) -> bool:
        return self.id >> 22 < snowflake.id >> 22
