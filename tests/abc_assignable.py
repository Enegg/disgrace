import disgrace.abc
from disgrace import ids
from disgrace.models.emoji import AppEmoji, GuildEmoji, UnicodeEmoji
from disgrace.models.guild import Guild
from disgrace.models.user import User
from disgrace.object import Object
from disgrace.structs import components, emoji
from disgrace.ui import ActionButton, LinkButton, PremiumButton


def assert_assignable(
    unicode_emoji: UnicodeEmoji,
    guild_emoji: GuildEmoji,
    app_emoji: AppEmoji,
    action_button: ActionButton,
    link_button: LinkButton,
    premium_button: PremiumButton,
    obj: Object,
    obj2: Object[ids.UserId],
    user: User,
    guild: Guild,
) -> None:
    # emoji
    _1: disgrace.abc.Emoji[None] = unicode_emoji
    _2: disgrace.abc.Emoji[ids.GuildEmojiId] = guild_emoji
    _3: disgrace.abc.Emoji[ids.AppEmojiId] = app_emoji
    _4: disgrace.abc.Snowflake[ids.GuildEmojiId] = guild_emoji
    _5: disgrace.abc.Snowflake[ids.AppEmojiId] = app_emoji
    _6: disgrace.abc.Partible[emoji.PartialEmoji] = unicode_emoji
    _7: disgrace.abc.Partible[emoji.PartialEmoji] = guild_emoji
    _8: disgrace.abc.Partible[emoji.PartialEmoji] = app_emoji

    # components
    _ = ActionButton(emoji=unicode_emoji, custom_id="")
    _ = ActionButton(emoji=guild_emoji, custom_id="")
    _ = ActionButton(emoji=app_emoji, custom_id="")
    _9: disgrace.abc.Destructible[components.RawButton] = action_button
    _10: disgrace.abc.Destructible[components.RawButton] = link_button
    _11: disgrace.abc.Destructible[components.RawButton] = premium_button

    # object
    _12: disgrace.abc.Snowflake[ids.SnowflakeId] = obj
    _13: disgrace.abc.Snowflake[ids.UserId] = obj2

    # user
    _14: disgrace.abc.Snowflake[ids.UserId] = user
    _15: disgrace.abc.User = user

    # guild
    _16: disgrace.abc.Snowflake[ids.GuildId] = guild
