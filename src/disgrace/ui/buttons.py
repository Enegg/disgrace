from typing import Literal

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.models.common import cast_str_id
from disgrace.structs import components
from disgrace.structs.components import ButtonStyleNS

__all__ = ("ActionButton", "LinkButton", "PremiumButton")

type AnyButton = ActionButton | LinkButton | PremiumButton


class ActionButton(msgspec.Struct, kw_only=True):
    """A UI button that emits an interaction."""

    type ActionButtonStyle = Literal[1, 2, 3, 4]

    id: int = 0
    custom_id: str
    style: ActionButtonStyle = ButtonStyleNS.secondary
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=self.style,
            label=self.label,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            custom_id=self.custom_id,
            disabled=self.disabled,
        )


class LinkButton(msgspec.Struct, kw_only=True):
    """A UI button that links to a URL."""

    id: int = 0
    url: str
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=ButtonStyleNS.link,
            label=self.label,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            url=self.url,
            disabled=self.disabled,
        )


class PremiumButton(msgspec.Struct, kw_only=True):
    """A UI button that represents a purchaseable SKU."""

    id: int = 0
    sku_id: ids.SkuId
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton(
            style=ButtonStyleNS.premium,
            sku_id=cast_str_id(self.sku_id),
            disabled=self.disabled,
        )
