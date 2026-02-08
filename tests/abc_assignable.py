import disgrace.abc
from disgrace import ids
from disgrace.models.emoji import AppEmoji, GuildEmoji, UnicodeEmoji
from disgrace.models.guild import Guild
from disgrace.models.user import User
from disgrace.object import Object
from disgrace.structs import components
from disgrace.ui import ActionButton, LinkButton, PremiumButton


def assert_assignable(
    unicode_emoji: UnicodeEmoji,
    guild_emoji: GuildEmoji,
    app_emoji: AppEmoji,
    action_button: ActionButton,
    link_button: LinkButton,
    premium_button: PremiumButton,
    obj: Object,
    user_obj: Object[ids.UserId],
    user: User,
    guild: Guild,
) -> None:
    # emoji
    _1: disgrace.abc.Emoji[None] = unicode_emoji
    _2: disgrace.abc.Emoji[ids.GuildEmojiId] = guild_emoji
    _3: disgrace.abc.Emoji[ids.AppEmojiId] = app_emoji
    _4: disgrace.abc.Snowflake = unicode_emoji  # pyright: ignore[reportAssignmentType]
    _5: disgrace.abc.Snowflake[ids.GuildEmojiId] = guild_emoji
    _6: disgrace.abc.Snowflake[ids.AppEmojiId] = app_emoji
    _7: disgrace.abc.Partible[emoji.PartialEmoji] = unicode_emoji
    _8: disgrace.abc.Partible[emoji.PartialEmoji] = guild_emoji
    _9: disgrace.abc.Partible[emoji.PartialEmoji] = app_emoji

    # components
    _10: disgrace.abc.Destructible[components.RawButton] = action_button
    _11: disgrace.abc.Destructible[components.RawButton] = link_button
    _12: disgrace.abc.Destructible[components.RawButton] = premium_button

    # object
    _13: disgrace.abc.Snowflake = obj
    _14: disgrace.abc.Snowflake[ids.UserId] = user_obj

    # user
    _15: disgrace.abc.Snowflake[ids.UserId] = user
    _16: disgrace.abc.User = user

    # guild
    _17: disgrace.abc.Snowflake[ids.GuildId] = guild
