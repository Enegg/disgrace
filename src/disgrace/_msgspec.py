import msgspec


class BaseStruct(msgspec.Struct, omit_defaults=True): ...


class BaseModel(msgspec.Struct, eq=False, frozen=True): ...
