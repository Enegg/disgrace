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


type Snowflake[IdT: SnowflakeId = SnowflakeId] = HasId[IdT]


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

    @abstractmethod
    def to_struct(self) -> StructT: ...


class Partible[PartialT](Protocol):
    """Object implementing `to_partial`."""

    __slots__ = ()

    @abstractmethod
    def to_partial(self) -> PartialT: ...
