from collections import abc
from typing import Literal

import msgspec

from . import raw_ids
from .emoji import RawGuildEmoji
from .misc import AssetHash, BaseStruct, Bitset, ISOTimestamp
from .sticker import RawSticker
from .user import RawAvatarDecorationData, RawUser

type RawVerificationLevel = Literal[0, 1, 2, 3, 4]
type RawDefaultMessageNotificationLevel = Literal[0, 1]
type RawRole = object


class RawMember(BaseStruct, kw_only=True):
    user: RawUser | msgspec.UnsetType = msgspec.UNSET
    nick: str | None = None
    avatar: AssetHash | None = None
    banner: AssetHash | None = None
    roles: abc.Sequence[raw_ids.RoleId]
    joined_at: ISOTimestamp
    premium_sice: ISOTimestamp | msgspec.UnsetType = msgspec.UNSET
    deaf: bool
    mute: bool
    flags: int = 0
    pending: bool = False
    permissions: str | msgspec.UnsetType = msgspec.UNSET
    communication_disabled_unitl: ISOTimestamp | None = None
    avatar_decoration_data: RawAvatarDecorationData | None = None


class RawWelcomeScreenChannel(BaseStruct, kw_only=True):
    channel_id: raw_ids.ChannelId
    description: str
    emoji_id: raw_ids.GuildEmojiId | None
    emoji_name: str | None


class RawWelcomeScreen(BaseStruct, kw_only=True):
    description: str | None
    welcome_channels: abc.Sequence[RawWelcomeScreenChannel]


class RawIncidentsData(BaseStruct, kw_only=True):
    invites_disabled_until: ISOTimestamp | None
    dms_disabled_until: ISOTimestamp | None
    dm_spam_detected_at: ISOTimestamp | None = None
    raid_detected_at: ISOTimestamp | None = None


class RawGuild(BaseStruct, kw_only=True):
    id: raw_ids.GuildId
    name: str
    icon: AssetHash | None
    icon_hash: AssetHash | None = None
    splash: AssetHash | None
    discovery_splash: AssetHash | None
    owner: bool = False
    owner_id: raw_ids.UserId
    permissions: Bitset | msgspec.UnsetType = msgspec.UNSET
    afk_channel_id: raw_ids.ChannelId | None
    afk_timeout: int
    widget_enabled: bool = False
    widget_channel_id: raw_ids.ChannelId | None = None
    verification_level: RawVerificationLevel
    default_message_notifications: RawDefaultMessageNotificationLevel
    explicit_content_filter: int  # TODO
    roles: abc.Sequence[RawRole]  # TODO: guild roles have some guarantees(?)
    emojis: abc.Sequence[RawGuildEmoji]
    features: abc.Sequence[str]
    mfa_level: int
    application_id: raw_ids.ApplicationId | msgspec.UnsetType = msgspec.UNSET
    system_channel_id: raw_ids.ChannelId | None
    system_channel_flags: int  # TODO
    rules_channel_id: raw_ids.ChannelId | None
    max_presences: int | None = None
    max_members: int | msgspec.UnsetType = msgspec.UNSET
    vanity_url_code: str | None
    description: str | None
    banner: AssetHash | None
    premium_tier: int
    premium_subscription_count: int | msgspec.UnsetType = msgspec.UNSET
    preferred_locale: str
    public_updates_channel_id: raw_ids.ChannelId | None
    max_video_channel_users: int | msgspec.UnsetType = msgspec.UNSET
    max_stage_video_channel_users: int | msgspec.UnsetType = msgspec.UNSET
    approximate_member_count: int | msgspec.UnsetType = msgspec.UNSET
    approximate_presence_count: int | msgspec.UnsetType = msgspec.UNSET
    welcome_screen: RawWelcomeScreen | msgspec.UnsetType = msgspec.UNSET
    nsfw_level: int
    stickers: abc.Sequence[RawSticker] | msgspec.UnsetType = msgspec.UNSET
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: raw_ids.ChannelId | None
    incidents_data: RawIncidentsData | None


class RawGuildPreview(BaseStruct, kw_only=True):
    id: str
    name: str
    icon: AssetHash | None
    splash: AssetHash | None
    discovery_splash: AssetHash | None
    emojis: abc.Sequence[RawGuildEmoji]
    features: abc.Sequence[str]
    approximate_member_count: int
    approximate_presence_count: int
    description: str | None
    stickers: abc.Sequence[RawSticker]
