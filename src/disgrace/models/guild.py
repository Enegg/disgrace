from collections import abc

import msgspec

from disgrace import ids
from disgrace.asset import Asset
from disgrace.enums import Locale

from .common import created_at
from .emoji import GuildEmoji
from .permissions import Permissions
from .role import Role


class Guild(msgspec.Struct, kw_only=True):
    id: ids.GuildId
    name: str
    icon: Asset.StaticOrGifAsset | None = None
    banner: Asset.StaticOrGifAsset | None = None
    splash: Asset.StaticAsset | None = None
    discovery_splash: Asset.StaticAsset | None = None
    owner_id: ids.UserId
    permissions: Permissions = msgspec.field(default_factory=Permissions)
    verification_level: int = 0
    default_message_notifications: int = 0
    explicit_content_filter: int = 0
    roles: abc.Sequence[Role] = ()
    emojis: abc.Sequence[GuildEmoji] = ()
    mfa_level: int = 0
    application_id: ids.ApplicationId | None = None
    system_channel_id: ids.ChannelId | None = None
    system_channel_flags: int = 0
    rules_channel_id: ids.ChannelId | None = None
    max_presences: int | None = None
    max_members: int = 0
    vanity_url_code: str | None = None
    description: str | None = None
    premium_tier: int = 0
    premium_subscription_count: int = 0
    preferred_locale: Locale = Locale.default
    approximate_member_count: int = 0
    approximate_presence_count: int = 0

    created_at = created_at
