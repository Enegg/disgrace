from typing import ClassVar, Self, override

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.asset import Asset
from disgrace.color import Color
from disgrace.enums import Locale, UserPremiumType
from disgrace.flags import UserFlags

from .common import created_at


class User(disgrace.abc.Mentionable, msgspec.Struct, kw_only=True):
    null: ClassVar[Self]

    id: ids.UserId
    username: str
    discriminator: str = "0"
    global_name: str | None = None
    avatar: Asset.StaticOrGifAsset | None = None
    bot: bool = False
    system: bool = False
    banner: Asset.StaticOrGifAsset | None = None
    accent_color: Color | None = None
    locale: Locale = Locale.default
    verified: bool = False
    flags: UserFlags = UserFlags.none
    premium_type: UserPremiumType = UserPremiumType.none
    public_flags: UserFlags = UserFlags.none

    created_at = created_at

    def __bool__(self) -> bool:
        return bool(self.id)

    @property
    @override
    def mention(self) -> str:
        return f"<@{self.id}>"

    @property
    def display_name(self) -> str:
        if self.global_name is not None:
            return self.global_name
        return self.username


User.null = User(
    id=ids.UserId(ids.SnowflakeId(0)),
    username="unknown-user",
    discriminator="0",
    global_name=None,
    avatar=None,
)
