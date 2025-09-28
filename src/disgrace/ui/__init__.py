from collections import abc

from disgrace.structs.components import (
    ButtonStyleNS,
    File,
    MediaGallery,
    MediaGalleryItem,
    Separator,
    TextDisplay,
    TextInputStyleNS,
    Thumbnail,
    UnfurledMediaItem,
)

from .buttons import ActionButton, AnyButton, LinkButton, PremiumButton
from .layout import ActionRow, Container, Section
from .modals import Label, TextInput
from .selects import (
    AnySelect,
    ChannelSelect,
    MentionableSelect,
    RoleSelect,
    SelectOption,
    StringSelect,
    UserSelect,
)

__all__ = (
    "ActionButton",
    "ActionRow",
    "ButtonStyleNS",
    "ChannelSelect",
    "Container",
    "File",
    "Label",
    "LinkButton",
    "MediaGallery",
    "MediaGalleryItem",
    "MentionableSelect",
    "PremiumButton",
    "RoleSelect",
    "Section",
    "SelectOption",
    "Separator",
    "StringSelect",
    "TextDisplay",
    "TextInput",
    "TextInputStyleNS",
    "Thumbnail",
    "TopLevelMessageComponent",
    "UnfurledMediaItem",
    "UserSelect",
)

type MessageComponents = abc.Sequence[abc.Sequence[AnyButton] | AnySelect]
type TopLevelMessageComponent = (
    ActionRow | Section | TextDisplay | MediaGallery | File | Separator | Container
)
