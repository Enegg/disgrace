from collections import abc

import msgspec

from disgrace._msgspec import BaseStruct

from . import raw_ids
from .common import AssetHash, Bitset, ISOTimestamp
from .emoji import RawGuildEmoji
from .user import RawAvatarDecorationData, RawUser

type RawRole = object


class RawMember(BaseStruct, kw_only=True):
    user: RawUser | msgspec.UnsetType = msgspec.UNSET
    nick: str | None = None
    avatar: AssetHash | None = None
    banner: AssetHash | None = None
    roles: abc.Sequence[raw_ids.RoleId]
    joined_at: ISOTimestamp
    flags: int = 0
    pending: bool = False
    permissions: str | msgspec.UnsetType = msgspec.UNSET
    communication_disabled_until: ISOTimestamp | None = None
    avatar_decoration_data: RawAvatarDecorationData | None = None


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
    roles: abc.Sequence[RawRole]  # TODO: guild roles have some guarantees(?)
    emojis: abc.Sequence[RawGuildEmoji]
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
    nsfw_level: int
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: raw_ids.ChannelId | None
