import datetime
from collections import abc

import msgspec

from disgrace import ids
from disgrace.asset import Asset
from disgrace.enums import Locale

from .common import created_at
from .emoji import GuildEmoji, UnicodeEmoji
from .permissions import Permissions

# TODO
type Role = object
type Feature = object
type Sticker = object


class WelcomeScreenChannel(msgspec.Struct, kw_only=True):
    channel_id: ids.ChannelId
    description: str
    emoji: GuildEmoji | UnicodeEmoji | None = None


class WelcomeScreen(msgspec.Struct, kw_only=True):
    description: str | None = None
    channels: abc.Sequence[WelcomeScreenChannel]


class IncidentsData(msgspec.Struct, kw_only=True):
    invites_disabled_until: datetime.datetime | None = None
    dms_disabled_until: datetime.datetime | None = None
    dm_spam_detected_at: datetime.datetime | None = None
    raid_detected_at: datetime.datetime | None = None


class Guild(msgspec.Struct, kw_only=True):
    id: ids.GuildId
    name: str
    icon: Asset.StaticOrGifAsset | None = None
    banner: Asset.StaticOrGifAsset | None = None
    splash: Asset.StaticAsset | None = None
    discovery_splash: Asset.StaticAsset | None = None
    owner_id: ids.UserId
    permissions: Permissions = msgspec.field(default_factory=Permissions)
    afk_channel_id: ids.ChannelId | None = None
    afk_timeout: int = 0
    widget_enabled: bool = False
    widget_channel_id: ids.ChannelId | None = None
    verification_level: int = 0
    default_message_notifications: int = 0
    explicit_content_filter: int = 0
    roles: abc.Sequence[Role] = ()
    emojis: abc.Sequence[GuildEmoji] = ()
    stickers: abc.Sequence[Sticker] = ()
    features: abc.Sequence[Feature] = ()
    mfa_level: int = 0
    application_id: ids.ApplicationId | None = None
    system_channel_id: ids.ChannelId | None = None
    system_channel_flags: int = 0
    rules_channel_id: ids.ChannelId | None = None
    max_presences: int | None = None
    max_members: int = 0
    vanity_url_code: str | None = None
    description: str | None = None
    banner: Asset.StaticOrGifAsset | None = None
    premium_tier: int = 0
    premium_subscription_count: int = 0
    preferred_locale: Locale = Locale.en_US
    public_updates_channel_id: ids.ChannelId | None = None
    safety_alerts_channel_id: ids.ChannelId | None = None
    max_video_channel_users: int = 0
    max_stage_video_channel_users: int = 0
    approximate_member_count: int = 0
    approximate_presence_count: int = 0
    welcome_screen: WelcomeScreen | None = None
    nsfw_level: int = 0
    premium_progress_bar_enabled: bool = False
    incidents_data: IncidentsData | None = None

    created_at = created_at
