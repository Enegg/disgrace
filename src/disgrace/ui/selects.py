from collections import abc

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace._msgspec import BaseModel
from disgrace.enums import ChannelType
from disgrace.models.common import cast_str_id
from disgrace.structs import components
from disgrace.utils import Range

__all__ = (
    "ChannelSelect",
    "MentionableSelect",
    "RoleSelect",
    "SelectOption",
    "StringSelect",
    "UserSelect",
)

type AnySelect = (
    StringSelect | UserSelect | RoleSelect | MentionableSelect | ChannelSelect
)


class SelectOption(BaseModel, frozen=True, kw_only=True):
    label: str
    value: str
    description: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    default: bool = False

    def to_struct(self) -> components.RawSelectOption:
        return components.RawSelectOption(
            label=self.label,
            value=self.value,
            description=self.description,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            default=self.default,
        )


class StringSelect(BaseModel, frozen=True, kw_only=True):
    id: int = 0
    custom_id: str
    options: abc.Sequence[SelectOption]
    placeholder: str = ""
    values_range: Range = Range(1, 1)
    disabled: bool = False

    def to_struct(self) -> components.RawStringSelect:
        return components.RawStringSelect(
            custom_id=self.custom_id,
            options=[option.to_struct() for option in self.options],
            placeholder=self.placeholder,
            min_values=self.values_range.min,
            max_values=self.values_range.max,
            disabled=self.disabled,
        )


class UserSelect(BaseModel, frozen=True, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    values_range: Range = Range(1, 1)
    disabled: bool = False

    def to_struct(self) -> components.RawUserSelect:
        return components.RawUserSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder,
            default_values=[
                components.RawSelectDefaultUserValue(id=cast_str_id(user.id))
                for user in self.default_users
            ]
            if self.default_users
            else msgspec.UNSET,
            min_values=self.values_range.min,
            max_values=self.values_range.max,
            disabled=self.disabled,
        )


class RoleSelect(BaseModel, frozen=True, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    values_range: Range = Range(1, 1)
    disabled: bool = False

    def to_struct(self) -> components.RawRoleSelect:
        return components.RawRoleSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder,
            default_values=[
                components.RawSelectDefaultRoleValue(id=cast_str_id(role.id))
                for role in self.default_roles
            ]
            if self.default_roles
            else msgspec.UNSET,
            min_values=self.values_range.min,
            max_values=self.values_range.max,
            disabled=self.disabled,
        )


class MentionableSelect(BaseModel, frozen=True, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    values_range: Range = Range(1, 1)
    disabled: bool = False

    def to_struct(self) -> components.RawMentionableSelect:
        default_values: list[
            components.RawSelectDefaultRoleValue | components.RawSelectDefaultUserValue
        ]
        default_values = [
            components.RawSelectDefaultRoleValue(id=cast_str_id(role.id))
            for role in self.default_roles
        ]
        # doesn't really matter if this is a list or generator comprehension
        default_values += [
            components.RawSelectDefaultUserValue(id=cast_str_id(user.id))
            for user in self.default_users
        ]
        return components.RawMentionableSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder,
            default_values=default_values or msgspec.UNSET,
            min_values=self.values_range.min,
            max_values=self.values_range.max,
            disabled=self.disabled,
        )


class ChannelSelect(BaseModel, frozen=True, kw_only=True):
    id: int = 0
    custom_id: str
    channel_types: abc.Collection[ChannelType]
    placeholder: str = ""
    default_channels: abc.Sequence[disgrace.abc.Snowflake[ids.ChannelId]] = ()
    values_range: Range = Range(1, 1)
    disabled: bool = False

    def to_struct(self) -> components.RawChannelSelect:
        return components.RawChannelSelect(
            custom_id=self.custom_id,
            channel_types=[type_.value for type_ in self.channel_types],
            placeholder=self.placeholder,
            default_values=[
                components.RawSelectDefaultChannelValue(id=cast_str_id(channel.id))
                for channel in self.default_channels
            ]
            if self.default_channels
            else msgspec.UNSET,
            min_values=self.values_range.min,
            max_values=self.values_range.max,
            disabled=self.disabled,
        )
