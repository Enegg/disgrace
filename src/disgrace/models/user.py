from typing import ClassVar, Self, override

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.asset import Asset, Png, StaticOrGif
from disgrace.color import Color
from disgrace.enums import Locale, UserPremiumType
from disgrace.flags import UserFlags

from .common import created_at


class AvatarDecoration(msgspec.Struct, kw_only=True):
    asset: Asset[Png]
    sku_id: ids.SkuId


class User(disgrace.abc.Mentionable, msgspec.Struct, kw_only=True):
    null: ClassVar[Self]

    id: ids.UserId
    username: str
    discriminator: str = "0"
    global_name: str | None = None
    avatar: Asset[StaticOrGif] | None = None
    bot: bool = False
    system: bool = False
    mfa_enabled: bool = False
    banner: Asset[StaticOrGif] | None = None
    accent_color: Color = Color.none
    locale: Locale = Locale.en_US
    verified: bool = False
    email: str | None = None
    flags: UserFlags = UserFlags.none
    premium_type: UserPremiumType = UserPremiumType.none
    public_flags: UserFlags = UserFlags.none
    avatar_decoration: AvatarDecoration | None = None

    __eq__ = disgrace.abc.Snowflake[ids.UserId].__eq__
    __hash__ = disgrace.abc.Snowflake[ids.UserId].__hash__
    created_at = created_at

    def __bool__(self) -> bool:
        return bool(self.id)

    @property
    @override
    def mention(self) -> str:
        return f"<@{self.id}>"


User.null = User(
    id=ids.UserId(ids.SnowflakeId(0)),
    username="unknown-user",
    discriminator="0",
    global_name=None,
    avatar=None,
)
