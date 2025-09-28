"""Various limits imposed by discord."""

from typing import Final, Never, final

from disgrace.utils import Range

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
    components: Final = 40
    """Maximum number of v2 components in a message."""
    file_size: Final = 10 << 20
    """Maximum size of each individual file, in bytes."""


@final
class ComponentLimits:
    """Limits imposed on UI components."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    custom_id: Final = 100
    """Maximum length of a component's custom ID."""
    action_row_buttons: Final = 5
    """Maximum number of buttons an ActionRow can have."""
    button_label: Final = 80
    """Maximum length of a button's label."""
    select_options: Final = Range(1, 25)
    """Maximum range of options a select menu can have."""
    select_placeholder: Final = 150
    """Maximum length of a select's placeholder."""
    select_min_max_values: Final = Range(0, 25)
    """Maximum range of values select menu's min_values/max_values can have."""
    select_option_label: Final = 100
    """Maximum length of a SelectOption's label."""
    select_option_value: Final = 100
    """Maximum length of a SelectOption's value."""
    select_option_description: Final = 100
    """Maximum length of a SelectOption's description."""
    text_input_value: Final = 4000
    """Maximum length of a TextInput's value."""
    text_input_placeholder: Final = 100
    """Maximum length of a TextInput's placeholder."""
    section_components_range: Final = Range(1, 3)
    """Maximum range of child components a Section can have."""
    media_description: Final = 1024
    """Maximum length of a media component's description."""
    gallery_items: Final = Range(1, 10)
    """Maximum range of items a MediaGallery can have."""
    label_label: Final = 45
    """Maximum length of a Label's label."""


@final
class InteractionLimits:
    """Limits imposed on responding to interactions."""

    __slots__ = ()

    def __new__(cls) -> Never: ...

    autocomplete_options: Final = 25
    """Maximum number of options an autocomplete can return."""
    response_timeout: Final = 3
    """Number of seconds until inital interaction times out."""
    deferred_response_timeout: Final = 60 * 15
    """Number of seconds an interaction remains valid for after deferring."""
