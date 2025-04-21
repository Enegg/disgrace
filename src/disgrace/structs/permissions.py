import msgspec

from disgrace import ids

from .misc import BaseStruct, StrBitset


class RawRoleTags(BaseStruct, kw_only=True):
    # None | UnsetType are just weird bools
    bot_id: ids.SnowflakeId  # "id of the bot"
    integration_id: ids.SnowflakeId | msgspec.UnsetType = msgspec.UNSET
    premium_subscriber: None | msgspec.UnsetType = msgspec.UNSET
    subscription_listing_id: ids.SnowflakeId | msgspec.UnsetType = msgspec.UNSET
    available_for_purchase: None | msgspec.UnsetType = msgspec.UNSET
    guild_connections: None | msgspec.UnsetType = msgspec.UNSET


class RawRole(BaseStruct, kw_only=True):
    id: ids.RoleId
    name: str
    color: int
    hoist: bool
    icon: str | None = None
    unicode_emoji: str | None = None
    position: int
    permissions: StrBitset
    managed: bool
    mentionable: bool
    tags: RawRoleTags | msgspec.UnsetType = msgspec.UNSET
    flags: int
