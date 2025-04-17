from typing import NewType

import msgspec

type BigInt = str | int
StrSnowflake = NewType("StrSnowflake", str)
ISOTimestamp = NewType("ISOTimestamp", str)
StrBitset = NewType("StrBitset", str)
IntBitset = NewType("IntBitset", int)
type Bitset = StrBitset | IntBitset
AssetHash = NewType("AssetHash", str)


class BaseStruct(msgspec.Struct, omit_defaults=True): ...
