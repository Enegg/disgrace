from typing import ClassVar, Literal

import msgspec

from disgrace.limits import ComponentLimits
from disgrace.structs import components

from .enums import ComponentType, TextInputStyle


class TextInput(msgspec.Struct, kw_only=True):
    type: ClassVar[Literal[ComponentType.text_input]] = ComponentType.text_input

    custom_id: str
    label: str
    style: TextInputStyle = TextInputStyle.short
    min_length: int = 0
    max_length: int = ComponentLimits.text_input_value
    required: bool = True
    value: str = ""
    placeholder: str = ""

    def to_struct(self) -> components.RawTextInput:
        return components.RawTextInput(
            custom_id=self.custom_id,
            style=self.style.value,
            label=self.label,
            min_length=self.min_length,
            max_length=self.max_length
            if self.max_length < ComponentLimits.text_input_value
            else msgspec.UNSET,
            required=self.required,
            value=self.value or msgspec.UNSET,
            placeholder=self.placeholder or msgspec.UNSET,
        )
