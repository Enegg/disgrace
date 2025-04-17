from abc import abstractmethod
from typing import Protocol, override

import msgspec

from disgrace.ids import SnowflakeId


class HasId[IdT: int](Protocol):
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
        return self.id >> 22


class Mentionable(Protocol):
    """Object with a `.mention` attribute. Implements `__str__`."""

    @property
    @abstractmethod
    def mention(self) -> str: ...

    @override
    def __str__(self) -> str:
        return self.mention


class Destructible[StructT: msgspec.Struct](Protocol):
    """Object implementing `to_struct`."""

    def to_struct(self) -> StructT: ...
