
import msgspec

from disgrace.structs import components
from disgrace.structs.components import TextInput

from .selects import AnySelect


class Label(msgspec.Struct, kw_only=True):
    """A layout UI component that wraps modal components."""

    type LabelComponent = TextInput | AnySelect

    id: int = 0
    label: str
    description: str = ""
    component: LabelComponent

    def to_struct(self) -> components.RawLabel:
        return components.RawLabel(
            id=self.id,
            label=self.label,
            description=self.description,
            component=self.component.to_struct(),
        )
