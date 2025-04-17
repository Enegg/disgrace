from typing import TYPE_CHECKING, SupportsInt

import attrs

import disgrace.abc
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

        def __init__(self, id: IdT | SupportsIntCast) -> None: ...


if True:
    def assert_assignable(obj: Object, obj2: Object[ids.UserId]) -> None:
        _1: disgrace.abc.Snowflake[ids.SnowflakeId] = obj
        _2: disgrace.abc.Snowflake[ids.UserId] = obj2
