# ruff: noqa: E501
import enum


# XXX: do we want flags to be ints?
# https://discord.com/developers/docs/resources/message#message-object-message-flags
class MessageFlags(enum.Flag):
    none = 0
    crossposted = 1 << 0
    """Message has been published to subscribed channels (via Channel Following)."""
    is_crosspost = 1 << 1
    """Message originates from a message in another channel (via Channel Following)."""
    suppress_embeds = 1 << 2
    """Do not include any embeds when serializing this message."""
    source_message_deleted = 1 << 3
    """The source message for this crosspost has been deleted (via Channel Following)."""
    urgent = 1 << 4
    """Message came from the urgent message system."""
    has_thread = 1 << 5
    """Message has an associated thread, with the same id as the message."""
    ephemeral = 1 << 6
    """Message is only visible to the user who invoked the Interaction."""
    loading = 1 << 7
    """Message is an Interaction Response and the bot is "thinking"."""
    failed_to_mention_some_roles_in_thread = 1 << 8
    """Message failed to mention some roles and add their members to the thread."""
    suppress_notifications = 1 << 12
    """Message will not trigger push and desktop notifications."""
    is_voice_message = 1 << 13
    """Message is a voice message."""
    has_snapshot = 1 << 14
    """Message has a snapshot (via Message Forwarding)."""

    silent = suppress_notifications
    """Alias for `.suppress_notifications`."""


class AttachmentFlags(enum.Flag):
    none = 0
    is_remix = 1 << 2
    """This attachment has been edited using the remix feature on mobile."""


class UserFlags(enum.Flag):
    none = 0
    staff = 1 << 0
    """Discord Employee."""
    partner = 1 << 1
    """Partnered Server Owner."""
    hypesquad = 1 << 2
    """HypeSquad Events Member."""
    bug_hunter_level_1 = 1 << 3
    """Bug Hunter Level 1."""
    hypesquad_online_house_1 = 1 << 6
    """House Bravery Member."""
    hypesquad_online_house_2 = 1 << 7
    """House Brilliance Member."""
    hypesquad_online_house_3 = 1 << 8
    """House Balance Member."""
    premium_early_supporter = 1 << 9
    """Early Nitro Supporter."""
    team_pseudo_user = 1 << 10
    """User is a [team](https://discord.com/developers/docs/topics/teams)."""
    bug_hunter_level_2 = 1 << 14
    """Bug Hunter Level 2."""
    verified_bot = 1 << 16
    """Verified Bot."""
    verified_developer = 1 << 17
    """Early Verified Bot Developer."""
    certified_moderator = 1 << 18
    """Moderator Programs Alumni."""
    bot_http_interactions = 1 << 19
    """Bot uses only [HTTP interactions](https://discord.com/developers/docs/interactions/receiving-and-responding#receiving-an-interaction) and is shown in the online member list."""
    active_developer = 1 << 22
    """User is an [Active Developer](https://support-dev.discord.com/hc/articles/10113997751447)."""


class ChannelFlags(enum.Flag):
    none = 0
    pinned = 1 << 1
    require_tag = 1 << 4
    hide_media_download_options = 1 << 15
