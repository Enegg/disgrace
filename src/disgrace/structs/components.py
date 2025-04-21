from collections import abc
from typing import Literal

import msgspec

from . import raw_ids
from .channel import RawChannelType
from .emoji import RawPartialEmoji
from .misc import BaseStruct

type RawComponentType = Literal[
    1,  # Action Row
    2,  # Button
    3,  # String Select
    4,  # Text Input
    5,  # User Select
    6,  # Role Select
    7,  # Mentionable Select
    8,  # Channel Select
]
type RawButtonStyle = Literal[
    1,  # primary
    2,  # secondary
    3,  # success
    4,  # danger
    5,  # link
    6,  # premium
]
type RawTextInputStyle = Literal[
    1,  # short
    2,  # paragraph
]
type AnyRawSelect = (
    RawStringSelect
    | RawUserSelect
    | RawRoleSelect
    | RawMentionableSelect
    | RawChannelSelect
)
type RawMessageComponent = RawButton | AnyRawSelect
type RawModalComponent = RawTextInput


class BaseComponent(BaseStruct, tag_field="type"): ...


class RawMessageActionRow(BaseComponent, tag=1, kw_only=True):
    components: abc.Sequence[RawMessageComponent]


class RawModalActionRow(BaseComponent, tag=1, kw_only=True):
    components: abc.Sequence[RawModalComponent]


# ---------------------------------------- button ----------------------------------------
class RawButton(BaseComponent, tag=2, kw_only=True):
    style: RawButtonStyle
    label: str | msgspec.UnsetType = msgspec.UNSET
    emoji: RawPartialEmoji | msgspec.UnsetType = msgspec.UNSET
    custom_id: str | msgspec.UnsetType = msgspec.UNSET
    sku_id: raw_ids.SkuId | msgspec.UnsetType = msgspec.UNSET
    url: str | msgspec.UnsetType = msgspec.UNSET
    disabled: bool = False


# --------------------------------------- selects ----------------------------------------
class RawSelectOption(BaseStruct, kw_only=True):
    label: str
    value: str
    description: str | msgspec.UnsetType = msgspec.UNSET
    emoji: RawPartialEmoji | msgspec.UnsetType = msgspec.UNSET
    default: bool = False


class RawStringSelect(BaseComponent, tag=3, kw_only=True):
    custom_id: str
    options: abc.Sequence[RawSelectOption]
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False


class RawSelectDefaultUserValue(BaseStruct, tag="user"):
    id: raw_ids.UserId


class RawSelectDefaultRoleValue(BaseStruct, tag="role"):
    id: raw_ids.RoleId


class RawSelectDefaultChannelValue(BaseStruct, tag="channel"):
    id: raw_ids.ChannelId


class RawUserSelect(BaseComponent, tag=5, kw_only=True):
    custom_id: str
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
    default_values: abc.Sequence[RawSelectDefaultUserValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False


class RawRoleSelect(BaseComponent, tag=6, kw_only=True):
    custom_id: str
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
    default_values: abc.Sequence[RawSelectDefaultRoleValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False


class RawMentionableSelect(BaseComponent, tag=7, kw_only=True):
    custom_id: str
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
    default_values: (
        abc.Sequence[RawSelectDefaultUserValue | RawSelectDefaultRoleValue]
        | msgspec.UnsetType
    ) = msgspec.UNSET
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False


class RawChannelSelect(BaseComponent, tag=8, kw_only=True):
    custom_id: str
    channel_types: abc.Sequence[RawChannelType]
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
    default_values: abc.Sequence[RawSelectDefaultChannelValue] | msgspec.UnsetType = (
        msgspec.UNSET
    )
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False


# -------------------------------------- text input --------------------------------------
class RawTextInput(BaseComponent, tag=4, kw_only=True):
    custom_id: str
    style: RawTextInputStyle
    label: str
    # https://jcristharif.com/msgspec/structs.html#omitting-default-values
    # according to above, non-container defaults are checked using `is` operator.
    # 0 is within range of interned ints, but max_length of 4000 is not.
    min_length: int = 0
    max_length: int | msgspec.UnsetType = msgspec.UNSET
    required: bool = True
    value: str | msgspec.UnsetType = msgspec.UNSET
    placeholder: str | msgspec.UnsetType = msgspec.UNSET
