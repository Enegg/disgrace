import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.models.common import cast_str_id
from disgrace.structs import components

__all__ = ("ActionButton", "LinkButton", "PremiumButton")

type AnyButton = ActionButton | LinkButton | PremiumButton


class ActionButton(msgspec.Struct, kw_only=True):
    """A UI button that emits an interaction."""

    custom_id: str
    id: int = 0
    style: components.ActionButtonStyle = components.ButtonStyleNS.secondary
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton.action_button(
            id=self.id,
            custom_id=self.custom_id,
            style=self.style,
            label=self.label,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            disabled=self.disabled,
        )


class LinkButton(msgspec.Struct, kw_only=True):
    """A UI button that links to a URL."""

    url: str
    id: int = 0
    label: str = ""
    emoji: disgrace.abc.PartialEmoji | None = None
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton.link_button(
            id=self.id,
            label=self.label,
            emoji=msgspec.UNSET if self.emoji is None else self.emoji.to_partial(),
            url=self.url,
            disabled=self.disabled,
        )


class PremiumButton(msgspec.Struct, kw_only=True):
    """A UI button that represents a purchaseable SKU."""

    sku_id: ids.SkuId
    id: int = 0
    disabled: bool = False

    def to_struct(self) -> components.RawButton:
        return components.RawButton.sku_button(
            id=self.id, sku_id=cast_str_id(self.sku_id), disabled=self.disabled
        )
