from typing import Final, Literal, Self, override

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.color import Color
from disgrace.enums import Locale, UserPremiumType
from disgrace.flags import UserFlags
from disgrace.null_objects import init_null


class User(disgrace.abc.Mentionable, msgspec.Struct, kw_only=True):
    id: ids.UserId
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool = False
    system: bool = False
    mfa_enabled: bool = False
    banner: str | None = None
    accent_color: Color = Color.none
    locale: Locale | None = None  # TODO: why can this be unset?
    verified: bool = False
    flags: UserFlags = UserFlags.none
    premium_type: UserPremiumType = UserPremiumType.none

    __eq__ = disgrace.abc.Snowflake[ids.UserId].__eq__
    __hash__ = disgrace.abc.Snowflake[ids.UserId].__hash__

    @property
    @override
    def mention(self) -> str:
        return f"<@{self.id}>"


@init_null
class NullUser(disgrace.abc.Mentionable):
    instance: Final[Self]  # pyright: ignore[reportGeneralTypeIssues]

    @property
    def id(self) -> ids.UserId:
        return ids.UserId(ids.SnowflakeId(0))

    @property
    @override
    def mention(self) -> str:
        return "<@0>"

    @property
    def username(self) -> str:
        return "Unknown"

    @property
    def discriminator(self) -> str:
        return "0"

    @property
    def global_name(self) -> str | None:
        return None

    @property
    def avatar(self) -> str | None:
        return None

    @property
    def bot(self) -> bool:
        return False

    @property
    def system(self) -> bool:
        return False

    @property
    def mfa_enabled(self) -> bool:
        return False

    @property
    def banner(self) -> str | None:
        return None

    @property
    def accent_color(self) -> Color | None:
        return None

    @property
    def locale(self) -> Locale | None:
        return None

    @property
    def verified(self) -> bool:
        return False

    @property
    def flags(self) -> UserFlags:
        return UserFlags.none

    @property
    def premium_type(self) -> UserPremiumType:
        return UserPremiumType.none

    def __bool__(self) -> Literal[False]:
        return False


if True:

    def assert_assignable(user: User, null_user: NullUser) -> None:
        _1: disgrace.abc.User = user
        _2: disgrace.abc.User = null_user
