from collections import abc
from typing import ClassVar, Literal

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.enums import ChannelType
from disgrace.structs import components

from .enums import ComponentType

__all__ = (
    "ChannelSelect",
    "MentionableSelect",
    "RoleSelect",
    "SelectOption",
    "StringSelect",
    "UserSelect",
)


class SelectOption(msgspec.Struct, kw_only=True):
    label: str
    value: str
    description: str = ""
    emoji: disgrace.abc.Emoji | None = None
    default: bool = False

    def to_struct(self) -> components.RawSelectOption:
        return components.RawSelectOption(
            label=self.label,
            value=self.value,
            description=self.description or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            default=self.default,
        )


class StringSelect(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.string_select]] = ComponentType.string_select
    custom_id: str
    options: abc.Sequence[SelectOption]
    placeholder: str = ""
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawStringSelect:
        return components.RawStringSelect(
            custom_id=self.custom_id,
            options=[option.to_struct() for option in self.options],
            placeholder=self.placeholder or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class UserSelect(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.user_select]] = ComponentType.user_select
    custom_id: str
    placeholder: str = ""
    default_values: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawUserSelect:
        return components.RawUserSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultUserValue(id=snowflake.id)
                for snowflake in self.default_values
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class RoleSelect(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.role_select]] = ComponentType.role_select
    custom_id: str
    placeholder: str = ""
    default_values: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawRoleSelect:
        return components.RawRoleSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultRoleValue(id=snowflake.id)
                for snowflake in self.default_values
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class MentionableSelect(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.mentionable_select]] = (
        ComponentType.mentionable_select
    )
    custom_id: str
    placeholder: str = ""
    default_values: abc.Sequence[
        disgrace.abc.Snowflake[ids.UserId] | disgrace.abc.Snowflake[ids.RoleId]
    ] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawMentionableSelect:
        return components.RawMentionableSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[] or msgspec.UNSET,  # TODO
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class ChannelSelect(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.channel_select]] = ComponentType.channel_select
    custom_id: str
    channel_types: abc.Collection[ChannelType]
    placeholder: str = ""
    default_values: abc.Sequence[disgrace.abc.Snowflake[ids.ChannelId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawChannelSelect:
        return components.RawChannelSelect(
            custom_id=self.custom_id,
            channel_types=[type_.value for type_ in self.channel_types],
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultChannelValue(id=snowflake.id)
                for snowflake in self.default_values
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )
