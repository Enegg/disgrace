"""Various limits imposed by discord."""

from typing import Final, Never, final

__all__ = ("ComponentLimits", "EmbedLimits", "InteractionLimits", "MessageLimits")


@final
class EmbedLimits:
    """Limits imposed on embeds & their sub-components."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    title: Final = 256
    """Maximum length of an embed's title."""
    description: Final = 4096
    """Maximum length of an embed's description."""
    fields: Final = 10
    """Maximum number of fields per embed."""
    field_name: Final = 256
    """Maximum length of an embed's field's name."""
    field_value: Final = 1024
    """Maximum length of an embed's field's value."""
    footer_text: Final = 2048
    """Maximum length of an embed's footer's text."""
    author_name: Final = 256
    """Maximum length of an embed's author's name."""
    total: Final = 6000
    """Maximum number of characters over all parts of an embed."""


@final
class MessageLimits:
    """Limits imposed on sending messages."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    content: Final = 2000
    """Maximum length of a message's content."""
    embeds: Final = 10
    """Maximum number of embeds per message."""
    files: Final = 10
    """Maximum number of files per message."""
    action_rows: Final = 5
    """Maximum number of action rows per message."""
    file_size: Final = 10 << 20
    """Maximum size of each individual file, in bytes."""


@final
class ComponentLimits:
    """Limits imposed on UI components."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    buttons_per_row: Final = 5
    """Maximum number of button components in a row."""
    custom_id: Final = 100
    """Maximum length of a component's custom id."""
    button_label: Final = 80
    """Maximum length of a button's label."""
    select_options: Final = 25
    """Maximum number of select options per string select menu."""
    select_placeholder: Final = 150
    """Maximum length of a select's placeholder."""
    select_option_label: Final = 100
    """Maximum length of a select option's label."""
    select_option_value: Final = 100
    """Maximum length of a select option's value."""
    select_option_description: Final = 100
    """Maximum length of a select option's description."""
    text_input_label: Final = 45
    """Maximum length of a text input's label."""
    text_input_value: Final = 4000
    """Maximum length of a text input's value."""
    text_input_placeholder: Final = 100
    """Maximum length of a text input's placeholder."""


@final
class InteractionLimits:
    """Limits imposed on responding to interactions."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    autocomplete_options: Final = 25
    """Maximum number of options an autocomplete can return."""
    response_timeout: Final = 3
    """Number of seconds until discord times out an interaction."""
    deferred_response_timeout: Final = 60 * 15
    """Number of seconds an interaction remains valid for after deferring."""
