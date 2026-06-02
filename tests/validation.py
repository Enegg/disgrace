import msgspec
import rich

from disgrace.ui.selects import SelectOption, StringSelect
from disgrace.ui.validation import validate_components
from disgrace.utils import Range

s = StringSelect(
    custom_id="123" * 34,
    options=(
        SelectOption(label="1" * 101, value="2" * 101, description="3" * 101),
        SelectOption(label="1", value="2", description="3" * 101),
    )
    + (SelectOption(label="1", value="2"),) * 25,
    values_range=Range(35, 70),
)
ctx = validate_components(s)
print("\n".join(map(str, ctx)))

rich.print(msgspec.to_builtins(s.to_struct()))
