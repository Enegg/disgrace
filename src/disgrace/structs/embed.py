from collections import abc
from typing import Literal

import msgspec

from .misc import ISOTimestamp

type RawEmbedType = Literal[
    "rich", "image", "video", "gifv", "article", "link", "poll_result"
]


class RawEmbedFooter(msgspec.Struct, kw_only=True):
    text: str
    icon_url: str | msgspec.UnsetType = msgspec.UNSET
    proxy_icon_url: str | msgspec.UnsetType = msgspec.UNSET


class RawEmbedMedia(msgspec.Struct, kw_only=True):
    url: str
    proxy_url: str | msgspec.UnsetType = msgspec.UNSET
    height: int | msgspec.UnsetType = msgspec.UNSET
    width: int | msgspec.UnsetType = msgspec.UNSET


class RawEmbedProvider(msgspec.Struct, kw_only=True):
    name: str | msgspec.UnsetType = msgspec.UNSET
    url: str | msgspec.UnsetType = msgspec.UNSET


class RawEmbedAuthor(msgspec.Struct, kw_only=True):
    name: str
    url: str | msgspec.UnsetType = msgspec.UNSET
    icon_url: str | msgspec.UnsetType = msgspec.UNSET
    proxy_icon_url: str | msgspec.UnsetType = msgspec.UNSET


class RawEmbedField(msgspec.Struct, omit_defaults=True, kw_only=True):
    name: str
    value: str
    inline: bool = True


class RawEmbed(msgspec.Struct, kw_only=True):
    title: str | msgspec.UnsetType = msgspec.UNSET
    type: RawEmbedType | msgspec.UnsetType = msgspec.UNSET
    description: str | msgspec.UnsetType = msgspec.UNSET
    url: str | msgspec.UnsetType = msgspec.UNSET
    timestamp: ISOTimestamp | msgspec.UnsetType = msgspec.UNSET
    color: int | msgspec.UnsetType = msgspec.UNSET
    footer: RawEmbedFooter | msgspec.UnsetType = msgspec.UNSET
    image: RawEmbedMedia | msgspec.UnsetType = msgspec.UNSET
    thumbnail: RawEmbedMedia | msgspec.UnsetType = msgspec.UNSET
    video: RawEmbedMedia | msgspec.UnsetType = msgspec.UNSET
    provider: RawEmbedProvider | msgspec.UnsetType = msgspec.UNSET
    author: RawEmbedAuthor | msgspec.UnsetType = msgspec.UNSET
    fields: abc.Sequence[RawEmbedField] | msgspec.UnsetType = msgspec.UNSET
