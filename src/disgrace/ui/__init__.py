from collections import abc

from .buttons import ActionButton, LinkButton, PremiumButton
from .enums import ButtonStyle, TextInputStyle
from .modals import TextInput
from .selects import (
    ChannelSelect,
    MentionableSelect,
    RoleSelect,
    StringSelect,
    UserSelect,
)

__all__ = (
    "ActionButton",
    "ButtonStyle",
    "ChannelSelect",
    "LinkButton",
    "MentionableSelect",
    "PremiumButton",
    "RoleSelect",
    "TextInput",
    "TextInputStyle",
    "UserSelect",
)

type AnyButton = ActionButton | LinkButton | PremiumButton
type AnySelect = (
    StringSelect | UserSelect | RoleSelect | MentionableSelect | ChannelSelect
)
type MessageComponents = abc.Sequence[abc.Sequence[AnyButton] | AnySelect]
type ModalComponents = abc.Sequence[TextInput]
