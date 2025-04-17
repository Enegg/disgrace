from typing import Literal

import msgspec

from disgrace import ids

type RawPremiumType = Literal[
    0,  # None
    1,  # Nitro Classic
    2,  # Nitro
    3,  # Nitro Basic
]

class RawAvatarDecorationData(msgspec.Struct, kw_only=True):
    asset: str
    sku_id: ids.SkuId


# TODO: class RawConnection
# TODO: class RawApplicationRoleConnection


class RawUser(msgspec.Struct, kw_only=True):
    id: ids.UserId
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool | msgspec.UnsetType = msgspec.UNSET
    system: bool | msgspec.UnsetType = msgspec.UNSET
    mfa_enabled: bool | msgspec.UnsetType = msgspec.UNSET
    banner: str | None | msgspec.UnsetType = msgspec.UNSET
    accent_color: int | None | msgspec.UnsetType = msgspec.UNSET
    locale: str | msgspec.UnsetType = msgspec.UNSET
    verified: bool | msgspec.UnsetType = msgspec.UNSET
    # email?: ?str
    flags: int | msgspec.UnsetType = msgspec.UNSET
    premium_type: RawPremiumType | msgspec.UnsetType = msgspec.UNSET
    public_flags: int = 0
    avatar_decoration_data: RawAvatarDecorationData | None = None
