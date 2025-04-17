from collections import abc
from typing import Literal

import msgspec

from disgrace import ids

from .emoji import RawGuildEmoji
from .misc import AssetHash, BaseStruct, ISOTimestamp
from .sticker import RawSticker
from .user import RawAvatarDecorationData, RawUser

type RawVerificationLevel = Literal[0, 1, 2, 3, 4]
type RawDefaultMessageNotificationLevel = Literal[0, 1]
type RawRole = object
type RawGuildFeature = str


class RawGuildMember(BaseStruct, kw_only=True):
    user: RawUser | msgspec.UnsetType = msgspec.UNSET
    nick: str | None = None
    avatar: AssetHash | None = None
    banner: AssetHash | None = None
    roles: abc.Sequence[ids.RoleId]
    joined_at: ISOTimestamp
    premium_sice: ISOTimestamp | msgspec.UnsetType = msgspec.UNSET
    deaf: bool
    mute: bool
    flags: int = 0
    pending: bool = False
    permissions: str | msgspec.UnsetType = msgspec.UNSET
    communication_disabled_unitl: ISOTimestamp | None = None
    avatar_decoration_data: RawAvatarDecorationData | None = None


class RawGuild(BaseStruct, kw_only=True):
    id: ids.GuildId
    name: str
    icon: AssetHash | None
    icon_hash: AssetHash | None = None
    splash: AssetHash | None
    discovery_splash: AssetHash | None
    owner: bool | msgspec.UnsetType = msgspec.UNSET
    owner_id: ids.UserId
    permissions: str | msgspec.UnsetType = msgspec.UNSET
    afk_channel_id: ids.ChannelId | None
    afk_timeout: int
    widget_enabled: bool | msgspec.UnsetType = msgspec.UNSET
    widget_channel_id: ids.ChannelId | None = None
    verification_level: RawVerificationLevel
    default_message_notifications: RawDefaultMessageNotificationLevel
    explicit_content_filter: int  # TODO
    roles: abc.Sequence[RawRole]  # TODO: guild roles have some guarantees(?)
    emojis: abc.Sequence[RawGuildEmoji]
    features: abc.Sequence[RawGuildFeature]
    mfa_level: int
    application_id: ids.ApplicationId | msgspec.UnsetType = msgspec.UNSET
    system_channel_id: ids.ChannelId | None
    system_channel_flags: int  # TODO
    rules_channel_id: ids.ChannelId | None
    max_presences: int | None = None
    max_members: int | msgspec.UnsetType = msgspec.UNSET
    vanity_url_code: str | None
    description: str | None
    banner: AssetHash | None
    premium_tier: int
    premium_subscription_count: int | msgspec.UnsetType = msgspec.UNSET


class RawGuildPreview(BaseStruct, kw_only=True):
    id: str
    name: str
    icon: AssetHash | None
    splash: AssetHash | None
    discovery_splash: AssetHash | None
    emojis: abc.Sequence[RawGuildEmoji]
    features: abc.Sequence[RawGuildFeature]
    approximate_member_count: int
    approximate_presence_count: int
    description: str | None
    stickers: abc.Sequence[RawSticker]
