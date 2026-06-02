from collections import abc

import msgspec

from disgrace.color import Color
from disgrace.structs import components as components_
from disgrace.structs.components import (
    File,
    MediaGallery,
    Separator,
    TextDisplay,
    Thumbnail,
)

from .buttons import AnyButton
from .selects import AnySelect


class ActionRow(msgspec.Struct, kw_only=True):
    """A layout UI component that contains a group of buttons or a select menu."""

    type ActionRowComponents = AnyButton | AnySelect

    id: int = 0
    components: abc.Sequence[ActionRowComponents]

    def to_struct(self) -> components_.RawActionRow:
        return components_.RawActionRow(
            id=self.id,
            components=[c.to_struct() for c in self.components],
        )


class Section(msgspec.Struct, kw_only=True):
    """A layout UI component that associates content with an accessory."""

    type SectionComponents = TextDisplay
    type SectionAccessory = AnyButton | Thumbnail

    id: int = 0
    components: abc.Sequence[SectionComponents]
    accessory: SectionAccessory

    def to_struct(self) -> components_.RawSection:
        return components_.RawSection(
            id=self.id,
            components=[c.to_struct() for c in self.components],
            accessory=self.accessory.to_struct(),
        )


class Container(msgspec.Struct, kw_only=True):
    """A layout UI component that encapsulates other components."""

    type ContainerComponents = (
        ActionRow | TextDisplay | Section | MediaGallery | Separator | File
    )

    id: int = 0
    components: abc.Sequence[ContainerComponents]
    accent_color: Color | None = None
    spoiler: bool = False

    def to_struct(self) -> components_.RawContainer:
        return components_.RawContainer(
            id=self.id,
            components=[c.to_struct() for c in self.components],
            accent_color=msgspec.UNSET
            if self.accent_color is None
            else self.accent_color.value,
            spoiler=self.spoiler,
        )
