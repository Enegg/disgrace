from typing import Protocol

from disgrace import ids
from disgrace.structs import emoji

from .structural import HasId, Mentionable, Partible

type AnyEmojiId = ids.AppEmojiId | ids.GuildEmojiId | None


class PartialEmoji[IdT: AnyEmojiId = AnyEmojiId](
    HasId[IdT], Partible[emoji.RawPartialEmoji], Protocol
):
    __slots__ = ()

    @property
    def name(self) -> str: ...
    @property
    def animated(self) -> bool: ...


class Emoji[IdT: AnyEmojiId = AnyEmojiId](
    HasId[IdT], Mentionable, Partible[emoji.RawPartialEmoji], Protocol
):
    __slots__ = ()

    @property
    def name(self) -> str: ...
    @property
    def animated(self) -> bool: ...
    @property
    def managed(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def require_colons(self) -> bool: ...
