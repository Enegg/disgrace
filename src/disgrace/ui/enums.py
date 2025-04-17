import enum


class ButtonStyle(enum.IntEnum):
    """Represents the style of a button component."""

    primary = 1
    secondary = 2
    success = 3
    danger = 4
    link = 5
    premium = 6

    blurple = 1
    """An alias for `.primary`."""
    gray = 2
    """An alias for `.secondary`."""
    green = 3
    """An alias for `.success`."""
    red = 4
    """An alias for `.danger`."""
    url = 5
    """An alias for `.link`."""
    sku = 6
    """An alias for `.premium`."""


class ComponentType(enum.IntEnum):
    action_row = 1
    button = 2
    string_select = 3
    text_input = 4
    user_select = 5
    role_select = 6
    mentionable_select = 7
    channel_select = 8


class TextInputStyle(enum.IntEnum):
    short = 1
    paragraph = 2

    single_line = 1
    """An alias for `.short`."""
    multiline = 2
    """An alias for `.paragraph`."""
    long = 2
    """An alias for `.paragraph`."""
