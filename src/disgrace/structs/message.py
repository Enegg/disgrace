from collections import abc
from typing import Literal

import msgspec

from . import raw_ids
from .channel import RawChannelType
from .components import RawActionRow
from .embed import RawEmbed
from .misc import ISOTimestamp
from .reaction import RawReaction
from .sticker import RawStickerItem
from .user import RawUser

type RawMessageType = Literal[
    0,  #  DEFAULT
    1,  #  RECIPIENT_ADD
    2,  #  RECIPIENT_REMOVE
    3,  #  CALL
    4,  #  CHANNEL_NAME_CHANGE
    5,  #  CHANNEL_ICON_CHANGE
    6,  #  CHANNEL_PINNED_MESSAGE
    7,  #  USER_JOIN
    8,  #  GUILD_BOOST
    9,  #  GUILD_BOOST_TIER_1
    10,  # GUILD_BOOST_TIER_2
    11,  # GUILD_BOOST_TIER_3
    12,  # CHANNEL_FOLLOW_ADD
    14,  # GUILD_DISCOVERY_DISQUALIFIED
    15,  # GUILD_DISCOVERY_REQUALIFIED
    16,  # GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING
    17,  # GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING
    18,  # THREAD_CREATED
    19,  # REPLY
    20,  # CHAT_INPUT_COMMAND
    21,  # THREAD_STARTER_MESSAGE
    22,  # GUILD_INVITE_REMINDER
    23,  # CONTEXT_MENU_COMMAND
    24,  # AUTO_MODERATION_ACTION
    25,  # ROLE_SUBSCRIPTION_PURCHASE
    26,  # INTERACTION_PREMIUM_UPSELL
    27,  # STAGE_START
    28,  # STAGE_END
    29,  # STAGE_SPEAKER
    31,  # STAGE_TOPIC
    32,  # GUILD_APPLICATION_PREMIUM_SUBSCRIPTION
    36,  # GUILD_INCIDENT_ALERT_MODE_ENABLED
    37,  # GUILD_INCIDENT_ALERT_MODE_DISABLED
    38,  # GUILD_INCIDENT_REPORT_RAID
    39,  # GUILD_INCIDENT_REPORT_FALSE_ALARM
    44,  # PURCHASE_NOTIFICATION
    46,  # POLL_RESULT
]


class RawChannelMention(msgspec.Struct, kw_only=True):
    id: raw_ids.ChannelId
    guild_id: raw_ids.GuildId
    type: RawChannelType
    name: str


class RawAttachment(msgspec.Struct, kw_only=True):
    id: raw_ids.AttachmentId
    filename: str
    title: str | msgspec.UnsetType = msgspec.UNSET
    description: str | msgspec.UnsetType = msgspec.UNSET
    content_type: str | msgspec.UnsetType = msgspec.UNSET
    size: int
    url: str
    proxy_url: str
    height: int | None = None
    width: int | None = None
    ephemeral: bool = False
    duration_secs: float | msgspec.UnsetType = msgspec.UNSET
    waveform: str | msgspec.UnsetType = msgspec.UNSET
    flags: int = 0


class RawMessage(msgspec.Struct, kw_only=True):
    id: raw_ids.MessageId
    channel_id: raw_ids.ChannelId
    author: RawUser
    content: str
    timestamp: ISOTimestamp
    edited_timestamp: str | None
    tts: bool
    mention_everyone: bool
    mentions: abc.Sequence[RawUser]
    mention_roles: abc.Sequence[raw_ids.RoleId]
    mention_channels: abc.Sequence[RawChannelMention] | msgspec.UnsetType = msgspec.UNSET
    attachments: abc.Sequence[RawAttachment]
    embeds: abc.Sequence[RawEmbed]
    reactions: abc.Sequence[RawReaction] | msgspec.UnsetType = msgspec.UNSET
    nonce: int | str | msgspec.UnsetType = msgspec.UNSET
    pinned: bool
    webhook_id: raw_ids.WebhookId | msgspec.UnsetType = msgspec.UNSET
    type: RawMessageType
    # activity?
    # application?
    application_id: raw_ids.ApplicationId | msgspec.UnsetType = msgspec.UNSET
    flags: int = 0
    # message_reference?
    # message_snapshots?
    # referenced_message?
    # interaction_metadata?
    # interaction? (deprecated)
    # thread?
    components: abc.Sequence[RawActionRow] | msgspec.UnsetType = msgspec.UNSET
    sticker_items: abc.Sequence[RawStickerItem] | msgspec.UnsetType = msgspec.UNSET
    # position?
    # role_subscription_data?
    # resolved?
    # poll?
    # call?
