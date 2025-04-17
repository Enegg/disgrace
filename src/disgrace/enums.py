# ruff: noqa: E501, N815
import enum


class MessageType(enum.IntEnum):
    default = 0
    recipient_add = 1
    recipient_remove = 2
    call = 3
    channel_name_change = 4
    channel_icon_change = 5
    channel_pinned_message = 6
    user_join = 7
    guild_boost = 8
    guild_boost_tier_1 = 9
    guild_boost_tier_2 = 10
    guild_boost_tier_3 = 11
    channel_follow_add = 12
    guild_discovery_disqualified = 14
    guild_discovery_requalified = 15
    guild_discovery_grace_period_initial_warning = 16
    guild_discovery_grace_period_final_warning = 17
    thread_created = 18
    reply = 19
    chat_input_command = 20
    thread_starter_message = 21
    guild_invite_reminder = 22
    context_menu_command = 23
    auto_moderation_action = 24
    role_subscription_purchase = 25
    interaction_premium_upsell = 26
    stage_start = 27
    stage_end = 28
    stage_speaker = 29
    stage_topic = 31
    guild_application_premium_subscription = 32
    guild_incident_alert_mode_enabled = 36
    guild_incident_alert_mode_disabled = 37
    guild_incident_report_raid = 38
    guild_incident_report_false_alarm = 39
    purchase_notification = 44
    poll_result = 46


class ChannelType(enum.IntEnum):
    guild_text = 0
    """A text channel within a server."""
    dm = 1
    """A direct message between users."""
    guild_voice = 2
    """A voice channel within a server."""
    group_dm = 3
    """A direct message between multiple users."""
    guild_category = 4
    """An [organizational category](https://support.discord.com/hc/en-us/articles/115001580171-Channel-Categories-101) that contains up to 50 channels."""
    guild_announcement = 5
    """A channel that [users can follow and crosspost into their own server](https://support.discord.com/hc/en-us/articles/360032008192) (formerly news channels)."""
    announcement_thread = 10
    """A temporary sub-channel within a `guild_announcement` channel."""
    public_thread = 11
    """A temporary sub-channel within a `guild_text` or `guild_forum` channel."""
    private_thread = 12
    """A temporary sub-channel within a `guild_text` channel that is only viewable by those invited and those with the MANAGE_THREADS permission."""
    guild_stage_voice = 13
    """A voice channel for [hosting events with an audience](https://support.discord.com/hc/en-us/articles/1500005513722)."""
    guild_directory = 14
    """The channel in a [hub](https://support.discord.com/hc/en-us/articles/4406046651927-Discord-Student-Hubs-FAQ) containing the listed servers."""
    guild_forum = 15
    """Channel that can only contain threads."""
    guild_media = 16
    """Channel that can only contain threads, similar to <code>guild_forum</code> channels."""


class UserPremiumType(enum.IntEnum):
    none = 0
    nitro_classic = 1
    nitro = 2
    nitro_basic = 3


# TODO: none locale?
class Locale(enum.StrEnum):
    bg = "bg"
    """The ``bg`` (Bulgarian) locale."""
    cs = "cs"
    """The ``cs`` (Czech) locale."""
    da = "da"
    """The ``da`` (Danish) locale."""
    de = "de"
    """The ``de`` (German) locale."""
    el = "el"
    """The ``el`` (Greek) locale."""
    en_GB = "en-GB"
    """The ``en-GB`` (English, UK) locale."""
    en_US = "en-US"
    """The ``en-US`` (English, US) locale."""
    es_ES = "es-ES"
    """The ``es-ES`` (Spanish) locale."""
    es_LATAM = "es-419"
    """The ``es-419`` (Spanish, LATAM) locale."""
    fi = "fi"
    """The ``fi`` (Finnish) locale."""
    fr = "fr"
    """The ``fr`` (French) locale."""
    hi = "hi"
    """The ``hi`` (Hindi) locale."""
    hr = "hr"
    """The ``hr`` (Croatian) locale."""
    hu = "hu"
    """The ``hu`` (Hungarian) locale."""
    id = "id"
    """The ``id`` (Indonesian) locale."""
    it = "it"
    """The ``it`` (Italian) locale."""
    ja = "ja"
    """The ``ja`` (Japanese) locale."""
    ko = "ko"
    """The ``ko`` (Korean) locale."""
    lt = "lt"
    """The ``lt`` (Lithuanian) locale."""
    nl = "nl"
    """The ``nl`` (Dutch) locale."""
    no = "no"
    """The ``no`` (Norwegian) locale."""
    pl = "pl"
    """The ``pl`` (Polish) locale."""
    pt_BR = "pt-BR"
    """The ``pt-BR`` (Portuguese) locale."""
    ro = "ro"
    """The ``ro`` (Romanian) locale."""
    ru = "ru"
    """The ``ru`` (Russian) locale."""
    sv_SE = "sv-SE"
    """The ``sv-SE`` (Swedish) locale."""
    th = "th"
    """The ``th`` (Thai) locale."""
    tr = "tr"
    """The ``tr`` (Turkish) locale."""
    uk = "uk"
    """The ``uk`` (Ukrainian) locale."""
    vi = "vi"
    """The ``vi`` (Vietnamese) locale."""
    zh_CN = "zh-CN"
    """The ``zh-CN`` (Chinese, China) locale."""
    zh_TW = "zh-TW"
    """The ``zh-TW`` (Chinese, Taiwan) locale."""
