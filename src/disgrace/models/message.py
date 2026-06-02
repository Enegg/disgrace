import datetime
from collections import abc

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.enums import MessageType
from disgrace.flags import AttachmentFlags, MessageFlags


class VisualMedia(msgspec.Struct, kw_only=True):
    height: int
    width: int


class AudioMedia(msgspec.Struct, kw_only=True):
    duration_secs: float
    waveform: str


class Attachment(msgspec.Struct, kw_only=True):
    id: ids.AttachmentId
    filename: str
    title: str = ""
    description: str = ""
    content_type: str = ""
    size: int
    url: str
    proxy_url: str
    media: VisualMedia | AudioMedia | None = None
    ephemeral: bool = False
    flags: AttachmentFlags = AttachmentFlags.none


class Message(msgspec.Struct, kw_only=True):
    id: ids.MessageId
    channel_id: ids.ChannelId
    author: disgrace.abc.User
    content: str
    created_at: datetime.datetime
    edited_at: datetime.datetime | None
    tts: bool
    mentions_everyone: bool
    mentions: abc.Sequence[disgrace.abc.User]
    role_mentions: abc.Sequence[ids.RoleId]
    channel_mentions: abc.Sequence[object] = ()
    attachments: abc.Sequence[Attachment]
    reactions: abc.Sequence[object] = ()
    # nonce
    pinned: bool
    type: MessageType
    # activity
    # application
    # application_id?: ids.ApplicationId
    flags: MessageFlags = MessageFlags.none
    # message_reference?
    # message_snapshots?
    # referenced_message?
    # interaction_metadata?
    # interaction? (deprecated)
    # thread?
    # components?
    # sticker_items?
    # stickers? (deprecated)
    # position?
    # role_subscription_data?
    # resolved?
    # poll?
    # call?


class WebhookMessage(msgspec.Struct, kw_only=True):
    id: ids.MessageId
    channel_id: ids.ChannelId
    author: disgrace.abc.WebhookUser

    webhook_id: ids.WebhookId


class InteractionMessage(msgspec.Struct, kw_only=True):
    id: ids.MessageId
    channel_id: ids.ChannelId
