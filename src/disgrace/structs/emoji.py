from collections import abc
from typing import Self

import msgspec

from . import raw_ids
from .misc import BaseStruct
from .user import RawUser


class RawPartialEmoji(BaseStruct, kw_only=True):
    id: raw_ids.AppEmojiId | raw_ids.GuildEmojiId | None
    name: str
    animated: bool = False

    def to_partial(self) -> Self:
        return self


class RawGuildEmoji(BaseStruct, kw_only=True):
    id: raw_ids.GuildEmojiId
    name: str
    roles: abc.Sequence[raw_ids.RoleId]
    user: RawUser | msgspec.UnsetType = msgspec.UNSET
    require_colons: bool | msgspec.UnsetType = msgspec.UNSET
    managed: bool | msgspec.UnsetType = msgspec.UNSET
    animated: bool | msgspec.UnsetType = msgspec.UNSET
    available: bool | msgspec.UnsetType = msgspec.UNSET
