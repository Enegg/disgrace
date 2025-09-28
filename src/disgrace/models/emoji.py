from collections import abc
from typing import Literal, override

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.asset import Asset
from disgrace.structs import emoji

from .common import cast_str_id, created_at

# TODO: cache unicode emojis?
_UNICODE_EMOJI_TABLE: abc.Mapping[str, "UnicodeEmoji"] = {}


class UnicodeEmoji(disgrace.abc.Mentionable, msgspec.Struct):
    name: str

    @property
    def id(self) -> None:
        return None

    @property
    def animated(self) -> Literal[False]:
        return False

    @property
    def managed(self) -> Literal[False]:
        return False

    @property
    def available(self) -> Literal[True]:
        return True

    @property
    def require_colons(self) -> Literal[False]:
        return False

    @override
    def __hash__(self) -> int:
        return hash(self.name)

    @property
    @override
    def mention(self) -> str:
        return self.name

    def to_partial(self) -> emoji.PartialEmoji:
        return emoji.PartialEmoji(id=None, name=self.name)


class GuildEmoji(disgrace.abc.Mentionable, msgspec.Struct):
    id: ids.GuildEmojiId
    name: str
    animated: bool = False
    managed: bool = False
    available: bool = True
    require_colons: bool = True

    __eq__ = disgrace.abc.Snowflake[ids.GuildEmojiId].__eq__
    __hash__ = disgrace.abc.Snowflake[ids.GuildEmojiId].__hash__
    created_at = created_at

    @property
    @override
    def mention(self) -> str:
        if self.animated:
            return f"<a:{self.name}:{self.id}>"
        return f"<:{self.name}:{self.id}>"

    def to_partial(self) -> emoji.PartialEmoji:
        return emoji.PartialEmoji(
            id=cast_str_id(self.id), name=self.name, animated=self.animated
        )

    def to_asset(self) -> Asset.StaticOrGifAsset:
        return Asset.from_emoji(self.id, self.animated)


class AppEmoji(disgrace.abc.Mentionable, msgspec.Struct):
    id: ids.AppEmojiId
    name: str
    animated: bool = False

    @property
    def managed(self) -> Literal[False]:
        return False

    @property
    def available(self) -> Literal[True]:
        return True

    @property
    def require_colons(self) -> Literal[True]:
        return True

    __eq__ = disgrace.abc.Snowflake[ids.AppEmojiId].__eq__
    __hash__ = disgrace.abc.Snowflake[ids.AppEmojiId].__hash__
    created_at = created_at

    @property
    @override
    def mention(self) -> str:
        if self.animated:
            return f"<a:{self.name}:{self.id}>"
        return f"<:{self.name}:{self.id}>"

    def to_partial(self) -> emoji.PartialEmoji:
        return emoji.PartialEmoji(
            id=cast_str_id(self.id), name=self.name, animated=self.animated
        )

    def to_asset(self) -> Asset.StaticOrGifAsset:
        return Asset.from_emoji(self.id, self.animated)
