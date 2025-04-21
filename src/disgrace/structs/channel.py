from collections import abc
from typing import Literal

import msgspec

from . import raw_ids
from .guild import RawMember
from .misc import ISOTimestamp
from .user import RawUser

type RawChannelType = Literal[
    0,  # guild_text
    1,  # dm
    2,  # guild_voice
    3,  # group_dm
    4,  # guild_category
    5,  # guild_announcement
    10,  # announcement_thread
    11,  # public_thread
    12,  # private_thread
    13,  # guild_stage_voice
    14,  # guild_directory
    15,  # guild_forum
    16,  # guild_media
]
type RawAutoArchiveDuration = Literal[
    60,  # 1h
    1440,  # 1d
    4320,  # 3d
    10080,  # 7d
]


class RawOverwrite(msgspec.Struct, kw_only=True):
    id: raw_ids.RoleId | raw_ids.UserId
    type: Literal[0, 1]
    allow: str
    deny: str


class RawThreadMetadata(msgspec.Struct, kw_only=True):
    archived: bool
    auto_archive_duration: RawAutoArchiveDuration
    archive_timestamp: ISOTimestamp
    locked: bool
    invitable: bool | msgspec.UnsetType = msgspec.UNSET
    create_timestamp: ISOTimestamp | None = None


class RawThreadMember(msgspec.Struct, kw_only=True):
    id: raw_ids.ChannelId | msgspec.UnsetType = msgspec.UNSET
    user_id: raw_ids.UserId | msgspec.UnsetType = msgspec.UNSET
    join_timestamp: ISOTimestamp
    flags: int
    member: RawMember | msgspec.UnsetType = msgspec.UNSET


class RawForumTag(msgspec.Struct, kw_only=True):
    id: raw_ids.SnowflakeId
    name: str
    moderated: bool
    emoji_id: raw_ids.GuildEmojiId | None = None
    emoji_name: str | None = None


class RawDefaultReaction(msgspec.Struct, kw_only=True):
    emoji_id: raw_ids.GuildEmojiId | None = None
    emoji_name: str | None = None


class RawChannel(msgspec.Struct, kw_only=True):
    id: raw_ids.ChannelId
    type: RawChannelType
    guild_id: raw_ids.GuildId | msgspec.UnsetType = msgspec.UNSET
    position: int | msgspec.UnsetType = msgspec.UNSET
    permission_overwrites: abc.Sequence[RawOverwrite] | msgspec.UnsetType = msgspec.UNSET
    name: str | None = None
    topic: str | None = None
    nsfw: bool = False
    last_message_id: raw_ids.MessageId | None = None
    bitrate: int | msgspec.UnsetType = msgspec.UNSET
    user_limit: int | msgspec.UnsetType = msgspec.UNSET
    rate_limit_per_user: int | msgspec.UnsetType = msgspec.UNSET
    recipients: abc.Sequence[RawUser] | msgspec.UnsetType = msgspec.UNSET
    icon: str | None = None
    owner_id: raw_ids.UserId | msgspec.UnsetType = msgspec.UNSET
    application_id: raw_ids.ApplicationId | msgspec.UnsetType = msgspec.UNSET
    managed: bool = False
    parent_id: raw_ids.ChannelId | None = None
    last_pin_timestamp: str | None = None
    rtc_region: str | None = None
    video_quality_mode: int = 1
    message_count: int | msgspec.UnsetType = msgspec.UNSET
    member_count: int | msgspec.UnsetType = msgspec.UNSET
    thread_metadata: RawThreadMetadata | msgspec.UnsetType = msgspec.UNSET
    member: RawThreadMember | msgspec.UnsetType = msgspec.UNSET
    default_auto_archive_duration: int | msgspec.UnsetType = msgspec.UNSET
    permissions: str | msgspec.UnsetType = msgspec.UNSET
    flags: int = 0
    total_message_sent: int | msgspec.UnsetType = msgspec.UNSET
    available_tags: abc.Sequence[RawForumTag] | msgspec.UnsetType = msgspec.UNSET
    applied_tags: abc.Sequence[raw_ids.SnowflakeId] | msgspec.UnsetType = msgspec.UNSET
    default_reaction_emoji: RawDefaultReaction | None = None
    default_thread_rate_limit_per_user: int | msgspec.UnsetType = msgspec.UNSET
    default_sort_order: int | None = None
    default_forum_layout: int = 0
