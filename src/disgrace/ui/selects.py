from collections import abc

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.enums import ChannelType
from disgrace.models.common import cast_str_id
from disgrace.structs import components

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


class SelectOption(msgspec.Struct, kw_only=True):
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


class StringSelect(msgspec.Struct, kw_only=True):
    id: int = 0
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
            placeholder=self.placeholder,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class UserSelect(msgspec.Struct, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawUserSelect:
        return components.RawUserSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder,
            default_values=[
                components.RawSelectDefaultUserValue(id=cast_str_id(user.id))
                for user in self.default_users
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class RoleSelect(msgspec.Struct, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawRoleSelect:
        return components.RawRoleSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder,
            default_values=[
                components.RawSelectDefaultRoleValue(id=cast_str_id(role.id))
                for role in self.default_roles
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class MentionableSelect(msgspec.Struct, kw_only=True):
    id: int = 0
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    min_values: int = 1
    max_values: int = 1
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
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )


class ChannelSelect(msgspec.Struct, kw_only=True):
    id: int = 0
    custom_id: str
    channel_types: abc.Collection[ChannelType]
    placeholder: str = ""
    default_channels: abc.Sequence[disgrace.abc.Snowflake[ids.ChannelId]] = ()
    min_values: int = 1
    max_values: int = 1
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
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )
