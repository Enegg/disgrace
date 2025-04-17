from typing import Literal

import attrs

type StaticFormatType = Literal["webp", "jpeg", "jpg", "png"]
type AssetFormatType = Literal["webp", "jpeg", "jpg", "png", "gif"]


@attrs.define(kw_only=True)
class Asset:
    url: str
    key: str
    animated: bool = False
