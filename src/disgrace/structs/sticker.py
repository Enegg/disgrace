from collections import abc
from typing import Literal

import msgspec

from . import raw_ids

type RawStickerType = Literal[
    1,  # standard
    2,  # guild
]
type RawStickerFormatType = Literal[
    1,  # png
    2,  # apng
    3,  # lottie
    4,  # gif
]


class RawSticker(msgspec.Struct, kw_only=True):
    id: raw_ids.StickerId
    pack_id: raw_ids.StickerPackId | msgspec.UnsetType = msgspec.UNSET
    name: str
    description: str | None
    tags: str
    type: RawStickerType
    format_type: RawStickerFormatType
    available: bool = True
    guild_id: raw_ids.GuildId | msgspec.UnsetType = msgspec.UNSET
    sort_value: int | msgspec.UnsetType = msgspec.UNSET


class RawStickerItem(msgspec.Struct, kw_only=True):
    id: raw_ids.StickerId
    name: str
    format_type: RawStickerFormatType


class RawStickerPack(msgspec.Struct, kw_only=True):
    id: raw_ids.StickerPackId
    stickers: abc.Sequence[RawSticker]
    name: str
    sku_id: raw_ids.SkuId
    cover_sticker_id: raw_ids.StickerId | msgspec.UnsetType = msgspec.UNSET
    description: str
    banner_asset_id: raw_ids.SnowflakeId | msgspec.UnsetType = msgspec.UNSET
    # TODO: figure what Snowflake this is about
    # "id of the sticker pack's banner image"
