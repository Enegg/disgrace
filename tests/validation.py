import msgspec
import rich

from disgrace.ui.selects import SelectOption, StringSelect
from disgrace.ui.validation import validate_components

s = StringSelect(
    custom_id="123" * 34,
    options=(
        SelectOption(label="1" * 101, value="2" * 101, description="3" * 101),
        SelectOption(label="1", value="2", description="3" * 101),
    )
    + (SelectOption(label="1", value="2"),) * 25,
    min_values=35,
    max_values=70,
)
ctx = validate_components(s)
print("\n".join(map(str, ctx)))

rich.print(msgspec.to_builtins(s.to_struct()))
