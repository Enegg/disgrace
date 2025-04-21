from typing import Literal

import msgspec

from . import raw_ids

type RawPremiumType = Literal[
    0,  # None
    1,  # Nitro Classic
    2,  # Nitro
    3,  # Nitro Basic
]

class RawAvatarDecorationData(msgspec.Struct, kw_only=True):
    asset: str
    sku_id: raw_ids.SkuId


# TODO: class RawConnection
# TODO: class RawApplicationRoleConnection


class RawUser(msgspec.Struct, kw_only=True):
    id: raw_ids.UserId
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool = False
    system: bool = False
    mfa_enabled: bool = False
    banner: str | None = None
    accent_color: int | None = None
    locale: str | msgspec.UnsetType = msgspec.UNSET
    verified: bool = False
    email: str | None = None
    flags: int = 0
    premium_type: RawPremiumType = 0
    public_flags: int = 0
    avatar_decoration_data: RawAvatarDecorationData | None = None
