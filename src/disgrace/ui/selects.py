from collections import abc

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.enums import ChannelType
from disgrace.limits import ComponentLimits
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


class SelectOption(msgspec.Struct, kw_only=True):
    label: str
    value: str
    description: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    default: bool = False

    def to_struct(self) -> components.RawSelectOption:
        if __debug__:
            self.validate()
        return components.RawSelectOption(
            label=self.label,
            value=self.value,
            description=self.description or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            default=self.default,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.label) > ComponentLimits.select_option_label:
            fields.append(f"{len(self.label)=} (> {ComponentLimits.select_option_label})")
        if len(self.value) > ComponentLimits.select_option_label:
            fields.append(f"{len(self.value)=} (> {ComponentLimits.select_option_value})")
        if len(self.description) > ComponentLimits.select_option_label:
            fields.append(f"{len(self.description)=} (> {ComponentLimits.select_option_description})")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class StringSelect(msgspec.Struct, kw_only=True):
    custom_id: str
    options: abc.Sequence[SelectOption]
    placeholder: str = ""
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawStringSelect:
        if __debug__:
            self.validate()
        return components.RawStringSelect(
            custom_id=self.custom_id,
            options=[option.to_struct() for option in self.options],
            placeholder=self.placeholder or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.placeholder) > ComponentLimits.select_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.select_placeholder})")  # noqa: E501
        if not 1 <= len(self.options) <= ComponentLimits.select_options:
            fields.append(f"{len(self.options)=} (∉ [1, {ComponentLimits.select_options}])")  # noqa: E501
        if not 0 <= self.min_values <= ComponentLimits.select_options:
            fields.append(f"{self.min_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.min_values > len(self.options):
            fields.append(f"{self.min_values=} (> {len(self.options)=})")
        if not 0 <= self.max_values <= ComponentLimits.select_options:
            fields.append(f"{self.max_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.max_values < len(self.options):
            fields.append(f"{self.max_values=} (< {len(self.options)=})")
        elif self.max_values > self.min_values:
            fields.append(f"{self.max_values=} (> {self.min_values=})")
        # fmt: on
        sub_fields: list[ValueError] = []

        for option in self.options:
            try:
                option.validate()

            except ValueError as exc:
                sub_fields.append(exc)

        if fields or sub_fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            if sub_fields:
                raise ExceptionGroup(msg, sub_fields)
            raise ValueError(msg)


class UserSelect(msgspec.Struct, kw_only=True):
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawUserSelect:
        if __debug__:
            self.validate()
        return components.RawUserSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultUserValue(id=cast_str_id(user.id))
                for user in self.default_users
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.placeholder) > ComponentLimits.select_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.select_placeholder})")  # noqa: E501
        if not 0 <= self.min_values <= ComponentLimits.select_options:
            fields.append(f"{self.min_values=} (∉ [0, {ComponentLimits.select_options}])")
        if not 0 <= self.max_values <= ComponentLimits.select_options:
            fields.append(f"{self.max_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.max_values > self.min_values:
            fields.append(f"{self.max_values=} (> {self.min_values=})")
        if self.default_users and not self.min_values <= len(self.default_users) <= self.max_values:  # noqa: E501
            fields.append(f"{len(self.default_users)=} (∉ [{self.min_values=}, {self.max_values=}])")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class RoleSelect(msgspec.Struct, kw_only=True):
    custom_id: str
    placeholder: str = ""
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawRoleSelect:
        if __debug__:
            self.validate()
        return components.RawRoleSelect(
            custom_id=self.custom_id,
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultRoleValue(id=cast_str_id(role.id))
                for role in self.default_roles
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.placeholder) > ComponentLimits.select_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.select_placeholder})")  # noqa: E501
        if not 0 <= self.min_values <= ComponentLimits.select_options:
            fields.append(f"{self.min_values=} (∉ [0, {ComponentLimits.select_options}])")
        if not 0 <= self.max_values <= ComponentLimits.select_options:
            fields.append(f"{self.max_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.max_values > self.min_values:
            fields.append(f"{self.max_values=} (> {self.min_values=})")
        if self.default_roles and not self.min_values <= len(self.default_roles) <= self.max_values:  # noqa: E501
            fields.append(f"{len(self.default_roles)=} (∉ [{self.min_values=}, {self.max_values=}])")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class MentionableSelect(msgspec.Struct, kw_only=True):
    custom_id: str
    placeholder: str = ""
    default_users: abc.Sequence[disgrace.abc.Snowflake[ids.UserId]] = ()
    default_roles: abc.Sequence[disgrace.abc.Snowflake[ids.RoleId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawMentionableSelect:
        if __debug__:
            self.validate()
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
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=default_values or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.placeholder) > ComponentLimits.select_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.select_placeholder})")  # noqa: E501
        if not 0 <= self.min_values <= ComponentLimits.select_options:
            fields.append(f"{self.min_values=} (∉ [0, {ComponentLimits.select_options}])")
        if not 0 <= self.max_values <= ComponentLimits.select_options:
            fields.append(f"{self.max_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.max_values > self.min_values:
            fields.append(f"{self.max_values=} (> {self.min_values=})")
        if (
            (self.default_users or self.default_roles)
            and not self.min_values <= len(self.default_users) + len(self.default_roles) <= self.max_values  # noqa: E501
        ):
            fields.append(f"{len(self.default_users) + len(self.default_roles)=} (∉ [{self.min_values=}, {self.max_values=}])")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class ChannelSelect(msgspec.Struct, kw_only=True):
    custom_id: str
    channel_types: abc.Collection[ChannelType]
    placeholder: str = ""
    default_channels: abc.Sequence[disgrace.abc.Snowflake[ids.ChannelId]] = ()
    min_values: int = 1
    max_values: int = 1
    disabled: bool = False

    def to_struct(self) -> components.RawChannelSelect:
        if __debug__:
            self.validate()
        return components.RawChannelSelect(
            custom_id=self.custom_id,
            channel_types=[type_.value for type_ in self.channel_types],
            placeholder=self.placeholder or msgspec.UNSET,
            default_values=[
                components.RawSelectDefaultChannelValue(id=cast_str_id(channel.id))
                for channel in self.default_channels
            ]
            or msgspec.UNSET,
            min_values=self.min_values,
            max_values=self.max_values,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.placeholder) > ComponentLimits.select_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.select_placeholder})")  # noqa: E501
        if not 0 <= self.min_values <= ComponentLimits.select_options:
            fields.append(f"{self.min_values=} (∉ [0, {ComponentLimits.select_options}])")
        if not 0 <= self.max_values <= ComponentLimits.select_options:
            fields.append(f"{self.max_values=} (∉ [0, {ComponentLimits.select_options}])")
        elif self.max_values > self.min_values:
            fields.append(f"{self.max_values=} (> {self.min_values=})")
        if self.default_channels and not self.min_values <= len(self.default_channels) <= self.max_values:  # noqa: E501
            fields.append(f"{len(self.default_channels)=} (∉ [{self.min_values=}, {self.max_values=}])")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)
