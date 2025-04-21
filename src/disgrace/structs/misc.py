from typing import NewType

import msgspec

type ISOTimestamp = str
StrBitset = NewType("StrBitset", str)
IntBitset = NewType("IntBitset", int)
type Bitset = StrBitset | IntBitset
AssetHash = NewType("AssetHash", str)


class BaseStruct(msgspec.Struct, omit_defaults=True): ...

