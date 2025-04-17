from typing import Literal

import msgspec

import disgrace.abc
from disgrace import ids
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

    style: ActionButtonStyle = ButtonStyle.secondary
    label: str = ""
    emoji: disgrace.abc.Emoji | None = None
    custom_id: str
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=self.style.value,
            label=self.label or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            custom_id=self.custom_id,
            disabled=self.disabled,
        )


class LinkButton(msgspec.Struct, kw_only=True):
    """A UI button that links to a URL."""

    label: str = ""
    emoji: disgrace.abc.Emoji | None = None
    url: str
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=ButtonStyle.link.value,
            label=self.label or msgspec.UNSET,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            url=self.url,
            disabled=self.disabled,
        )


class PremiumButton(msgspec.Struct, kw_only=True):
    """A UI button that represents a purchaseable SKU."""

    sku_id: ids.SkuId
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=ButtonStyle.premium.value,
            sku_id=self.sku_id,
            disabled=self.disabled,
        )
