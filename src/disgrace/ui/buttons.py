from typing import Literal

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.limits import ComponentLimits
from disgrace.models.common import cast_str_id
from disgrace.structs import components

from .enums import ButtonStyle

__all__ = ("ActionButton", "LinkButton", "PremiumButton")


type ActionButtonStyle = Literal[
    ButtonStyle.primary,
    ButtonStyle.secondary,
    ButtonStyle.success,
    ButtonStyle.danger,
]


class ActionButton(msgspec.Struct, kw_only=True):
    """A UI button that emits an interaction."""

    custom_id: str
    style: ActionButtonStyle = ButtonStyle.secondary
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        if __debug__:
            self.validate()
        return components.RawButton(
            style=self.style.value,
            label=self.label or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            custom_id=self.custom_id,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.label) > ComponentLimits.button_label:
            fields.append(f"{len(self.label)=} (> {ComponentLimits.button_label})")
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class LinkButton(msgspec.Struct, kw_only=True):
    """A UI button that links to a URL."""

    url: str
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        if __debug__:
            self.validate()
        return components.RawButton(
            style=ButtonStyle.link.value,
            label=self.label or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            url=self.url,
            disabled=self.disabled,
        )

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.label) > ComponentLimits.button_label:
            fields.append(f"{len(self.label)=} (> {ComponentLimits.button_label})")
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)


class PremiumButton(msgspec.Struct, kw_only=True):
    """A UI button that represents a purchaseable SKU."""

    sku_id: ids.SkuId
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=ButtonStyle.premium.value,
            sku_id=cast_str_id(self.sku_id),
            disabled=self.disabled,
        )
