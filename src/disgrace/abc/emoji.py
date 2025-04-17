from typing import Protocol

from disgrace import ids
from disgrace.structs import emoji

from .structural import Mentionable

type AnyEmojiId = ids.AppEmojiId | ids.GuildEmojiId | None


class Emoji[IdT: AnyEmojiId = AnyEmojiId](Mentionable, Protocol):
    @property
    def id(self) -> IdT: ...
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

    def to_partial(self) -> emoji.RawPartialEmoji: ...
