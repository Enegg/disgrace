from typing import NewType

type ISOTimestamp = str
StrBitset = NewType("StrBitset", str)
IntBitset = NewType("IntBitset", int)
type Bitset = StrBitset | IntBitset
AssetHash = NewType("AssetHash", str)
