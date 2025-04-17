from collections import abc

import msgspec

from disgrace import ids

from .misc import BaseStruct
from .user import RawUser


class RawPartialEmoji(BaseStruct, kw_only=True):
    id: ids.AppEmojiId | ids.GuildEmojiId | None
    name: str
    animated: bool = False


class RawGuildEmoji(BaseStruct, kw_only=True):
    id: ids.GuildEmojiId
    name: str
    roles: abc.Sequence[ids.RoleId]
    user: RawUser | msgspec.UnsetType = msgspec.UNSET
    require_colons: bool | msgspec.UnsetType = msgspec.UNSET
    managed: bool | msgspec.UnsetType = msgspec.UNSET
    animated: bool | msgspec.UnsetType = msgspec.UNSET
    available: bool | msgspec.UnsetType = msgspec.UNSET


class RawEmoji(BaseStruct, kw_only=True): ...
