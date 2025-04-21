from abc import abstractmethod
from typing import Protocol, override

import msgspec

from disgrace.ids import SnowflakeId


class HasId[IdT](Protocol):
    """Object with an `.id` attribute."""

    __slots__ = ()

    @property
    @abstractmethod
    def id(self) -> IdT: ...


class Snowflake[IdT: SnowflakeId](HasId[IdT], Protocol):
    """A generic, unique discord object. Implements `__eq__`, `__hash__`."""

    __slots__ = ()

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.id == other.id

    @override
    def __hash__(self) -> int:
        # Snowflake IDs are uint64. Python's ints hash to themselves
        # up to (1 << 61) - 2, which is 0x...1110
        # the leading 0 means we effectively have 60 bits to work with
        return self.id >> 4


class Mentionable(Protocol):
    """Object with a `.mention` attribute. Implements `__str__`."""

    __slots__ = ()

    @property
    @abstractmethod
    def mention(self) -> str: ...

    @override
    def __str__(self) -> str:
        return self.mention


class Destructible[StructT: msgspec.Struct | msgspec.UnsetType](Protocol):
    """Object implementing `to_struct`."""

    __slots__ = ()

    def to_struct(self) -> StructT: ...


class Partible[PartialT](Protocol):
    """Object implementing `to_partial`."""

    __slots__ = ()

    def to_partial(self) -> PartialT: ...
