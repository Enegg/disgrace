from typing import Final, Protocol, Self


class NullObject(Protocol):
    instance: Final[Self]


def init_null[ObjT: NullObject](cls: type[ObjT], /) -> type[ObjT]:
    def __new__(cls: type[ObjT]) -> ObjT:  # noqa: N807
        return cls.instance

    cls.__new__ = __new__
    cls.instance = object.__new__(cls)  # pyright: ignore[reportAttributeAccessIssue]
    return cls
