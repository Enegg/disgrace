
import msgspec

from disgrace.limits import ComponentLimits
from disgrace.structs import components

from .enums import TextInputStyle


class TextInput(msgspec.Struct, kw_only=True):
    custom_id: str
    label: str
    style: TextInputStyle = TextInputStyle.short
    min_length: int = 0
    max_length: int = ComponentLimits.text_input_value
    required: bool = True
    value: str = ""
    placeholder: str = ""

    def to_struct(self) -> components.RawTextInput:
        if __debug__:
            self.validate()
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

    def validate(self) -> None:
        fields: list[str] = []
        # fmt: off
        if len(self.custom_id) > ComponentLimits.custom_id:
            fields.append(f"{len(self.custom_id)=} (> {ComponentLimits.custom_id})")
        if len(self.label) > ComponentLimits.text_input_label:
            fields.append(f"{len(self.label)=} (> {ComponentLimits.text_input_label})")
        if len(self.placeholder) > ComponentLimits.text_input_placeholder:
            fields.append(f"{len(self.placeholder)=} (> {ComponentLimits.text_input_placeholder})")  # noqa: E501
        if not 0 <= self.min_length <= ComponentLimits.text_input_value:
            fields.append(f"{self.min_length=} (∉ [0, {ComponentLimits.text_input_value}])")  # noqa: E501
        if not 0 <= self.max_length <= ComponentLimits.text_input_value:
            fields.append(f"{self.max_length=} (∉ [0, {ComponentLimits.text_input_value}])")  # noqa: E501
        elif self.max_length > self.min_length:
            fields.append(f"{self.max_length=} (> {self.min_length=})")
        if self.value and not self.min_length <= len(self.value) <= self.max_length:
            fields.append(f"{len(self.value)=} (∉ [{self.min_length=}, {self.max_length=}])")  # noqa: E501
        # fmt: on
        if fields:
            msg = f"Invalid values in {self!r}:\n{'\n'.join(fields)}"
            raise ValueError(msg)
