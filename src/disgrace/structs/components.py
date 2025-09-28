from collections import abc
from typing import Any, ClassVar, Final, Literal, Self, final

import msgspec

from disgrace.limits import ComponentLimits
from disgrace.utils import Namespace

from . import raw_ids
from .channel import RawChannelType
from .emoji import PartialEmoji
from .misc import BaseStruct

type ComponentType = Literal[
    1,  # Action Row
    2,  # Button
    3,  # String Select
    4,  # Text Input
    5,  # User Select
    6,  # Role Select
    7,  # Mentionable Select
    8,  # Channel Select
    9,  # Section
    10,  # Text Display
    11,  # Thumbnail
    12,  # Media Gallery
    13,  # File
    14,  # Separator
    # ...
    17,  # Container
    18,  # Label
]


@final
class ComponentTypeNS(Namespace):
    """Represents the type of UI components."""

    __slots__ = ()

    action_row: Final = 1
    button: Final = 2
    string_select: Final = 3
    text_input: Final = 4
    user_select: Final = 5
    role_select: Final = 6
    mentionable_select: Final = 7
    channel_select: Final = 8
    section: Final = 9
    text_display: Final = 10
    thumbnail: Final = 11
    media_gallery: Final = 12
    file: Final = 13
    separator: Final = 14
    # ...
    container: Final = 17
    label: Final = 18


type ButtonStyle = Literal[
    1,  # primary
    2,  # secondary
    3,  # success
    4,  # danger
    5,  # link
    6,  # premium
]


@final
class ButtonStyleNS(Namespace):
    """Represents the style of a button component."""

    __slots__ = ()

    primary: Final = 1
    secondary: Final = 2
    success: Final = 3
    danger: Final = 4
    link: Final = 5
    premium: Final = 6

    blurple: Final = 1
    """An alias for `.primary`."""
    gray: Final = 2
    """An alias for `.secondary`."""
    green: Final = 3
    """An alias for `.success`."""
    red: Final = 4
    """An alias for `.danger`."""
    url: Final = 5
    """An alias for `.link`."""
    sku: Final = 6
    """An alias for `.premium`."""


type TextInputStyle = Literal[
    1,  # short
    2,  # paragraph
]


@final
class TextInputStyleNS(Namespace):
    """Represents the style of a TextInput component."""

    __slots__ = ()

    short: Final = 1
    paragraph: Final = 2

    single_line: Final = 1
    """An alias for `.short`."""
    multiline: Final = 2
    """An alias for `.paragraph`."""
    long: Final = 2
    """An alias for `.paragraph`."""


type SeparatorSpacing = Literal[
    1,  # small
    2,  # large
]


@final
class SeparatorSpacingNS(Namespace):
    """Represents the spacing of a Separator component."""

    __slots__ = ()

    small: Final = 1
    large: Final = 2


class BaseComponent(BaseStruct, tag_field="type"):
    # TODO: ReadOnly[ClassVar[LiteralComponentType]]
    type: ClassVar[Any | int]


# -------------------------------------- action row --------------------------------------
type AnyRawSelect = (
    RawStringSelect
    | RawUserSelect
    | RawRoleSelect
    | RawMentionableSelect
    | RawChannelSelect
)
type RawActionRowChild = RawButton | AnyRawSelect


class RawActionRow(BaseComponent, tag=ComponentTypeNS.action_row, kw_only=True):
    type: ClassVar[Literal[1]]
    id: int = 0
    components: abc.Sequence[RawActionRowChild]


# ---------------------------------------- button ----------------------------------------
class RawButton(BaseComponent, tag=ComponentTypeNS.button, kw_only=True):
    type: ClassVar[Literal[2]]
    id: int = 0
    style: ButtonStyle
    label: str = ""
    emoji: PartialEmoji | msgspec.UnsetType = msgspec.UNSET
    custom_id: str = ""
    sku_id: raw_ids.SkuId | msgspec.UnsetType = msgspec.UNSET
    url: str = ""
    disabled: bool = False


# ------------------------------------ string select -------------------------------------
class RawSelectOption(BaseStruct, kw_only=True):
    label: str
    value: str
    description: str = ""
    emoji: PartialEmoji | msgspec.UnsetType = msgspec.UNSET
    default: bool = False


class RawStringSelect(BaseComponent, tag=ComponentTypeNS.string_select, kw_only=True):
    type: ClassVar[Literal[3]]
    id: int = 0
    custom_id: str
    options: abc.Sequence[RawSelectOption]
    placeholder: str = ""
    min_values: int = 1
    max_values: int = 1
    required: bool = True
    disabled: bool = False


# -------------------------------------- text input --------------------------------------
class TextInput(BaseComponent, tag=ComponentTypeNS.text_input, kw_only=True):
    """An interactive UI component that enables free-form text input in modals."""

    type: ClassVar[Literal[4]]
    id: int = 0
    custom_id: str
    style: TextInputStyle
    # https://jcristharif.com/msgspec/structs.html#omitting-default-values
    # according to above, non-container defaults are checked using `is` operator.
    # 0 is within range of interned ints, but max_length of 4000 is not.
    min_length: int = 0
    max_length: int = ComponentLimits.text_input_value
    required: bool = True
    value: str = ""
    placeholder: str = ""

    def to_struct(self) -> Self:
        return self


# ---------------------- user / role / mentionable / channel select ----------------------
class RawSelectDefaultUserValue(BaseStruct, tag_field="type", tag="user"):
    type: ClassVar[Literal["user"]]
    id: raw_ids.UserId


class RawSelectDefaultRoleValue(BaseStruct, tag_field="type", tag="role"):
    type: ClassVar[Literal["role"]]
    id: raw_ids.RoleId


class RawSelectDefaultChannelValue(BaseStruct, tag_field="type", tag="channel"):
    type: ClassVar[Literal["channel"]]
    id: raw_ids.ChannelId


class RawUserSelect(BaseComponent, tag=ComponentTypeNS.user_select, kw_only=True):
    type: ClassVar[Literal[5]]
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_values: abc.Sequence[RawSelectDefaultUserValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    required: bool = True
    disabled: bool = False


class RawRoleSelect(BaseComponent, tag=6, kw_only=True):
    type: ClassVar[Literal[6]]
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_values: abc.Sequence[RawSelectDefaultRoleValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    required: bool = True
    disabled: bool = False


class RawMentionableSelect(BaseComponent, tag=7, kw_only=True):
    type: ClassVar[Literal[7]]
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_values: (
        abc.Sequence[RawSelectDefaultUserValue | RawSelectDefaultRoleValue]
        | msgspec.UnsetType
    ) = msgspec.UNSET
    min_values: int = 1
    max_values: int = 1
    required: bool = True
    disabled: bool = False


class RawChannelSelect(BaseComponent, tag=8, kw_only=True):
    type: ClassVar[Literal[8]]
    id: int = 0
    custom_id: str
    channel_types: abc.Sequence[RawChannelType]
    placeholder: str = ""
    default_values: abc.Sequence[RawSelectDefaultChannelValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    required: bool = True
    disabled: bool = False


# --------------------------------------- section ----------------------------------------
type RawSectionChild = TextDisplay
type RawSectionAccessory = RawButton | Thumbnail


class RawSection(BaseComponent, tag=9, kw_only=True):
    type: ClassVar[Literal[9]]
    id: int = 0
    components: abc.Sequence[RawSectionChild]
    accessory: RawSectionAccessory


# ------------------------------------- text display -------------------------------------
class TextDisplay(BaseComponent, tag=10, kw_only=True):
    """A content UI component that can display markdown formatted text."""

    type: ClassVar[Literal[10]]
    id: int = 0
    content: str

    def to_struct(self) -> Self:
        return self


# -------------------------------------- thumbnail ---------------------------------------
class UnfurledMediaItem(BaseStruct, kw_only=True):
    url: str


class Thumbnail(BaseComponent, tag=11, kw_only=True):
    """A content UI component that displays visual media in a small form-factor."""

    type: ClassVar[Literal[11]]
    id: int = 0
    media: UnfurledMediaItem
    description: str = ""
    spoiler: bool = False

    def to_struct(self) -> Self:
        return self


# ------------------------------------ media gallery -------------------------------------
class MediaGalleryItem(BaseStruct, kw_only=True):
    """Element of a MediaGallery."""

    media: UnfurledMediaItem
    description: str = ""
    spoiler: bool = False


class MediaGallery(BaseComponent, tag=12, kw_only=True):
    """A content UI component that allows you to display multiple media attachments."""

    type: ClassVar[Literal[12]]
    id: int = 0
    items: abc.Sequence[MediaGalleryItem]

    def to_struct(self) -> Self:
        return self


# ----------------------------------------- file -----------------------------------------
class File(BaseComponent, tag=13, kw_only=True):
    """A content UI component that allows you to display an uploded file."""

    type: ClassVar[Literal[13]]
    id: int = 0
    file: UnfurledMediaItem
    spoiler: bool = False

    def to_struct(self) -> Self:
        return self


# -------------------------------------- separator ---------------------------------------
class Separator(BaseComponent, tag=14, kw_only=True):
    """A layout UI component that adds vertical padding and visual division."""

    type: ClassVar[Literal[14]]
    id: int = 0
    divider: bool = True
    spacing: SeparatorSpacing = SeparatorSpacingNS.small

    def to_struct(self) -> Self:
        return self


# -------------------------------------- container ---------------------------------------
type RawContainerChild = (
    RawActionRow | TextDisplay | RawSection | MediaGallery | Separator | File
)


class RawContainer(BaseComponent, tag=17, kw_only=True):
    type: ClassVar[Literal[17]]
    id: int = 0
    components: abc.Sequence[RawContainerChild]
    # #000000 is a valid color
    accent_color: int | msgspec.UnsetType = msgspec.UNSET
    spoiler: bool = False


# ---------------------------------------- label -----------------------------------------
type RawLabelChild = TextInput | AnyRawSelect


class RawLabel(BaseComponent, tag=18, kw_only=True):
    type: ClassVar[Literal[18]]
    id: int = 0
    label: str
    description: str = ""
    component: RawLabelChild
