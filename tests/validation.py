from disgrace.ui.selects import SelectOption, StringSelect

s = StringSelect(
    custom_id="123" * 34,
    options=(
        SelectOption(label="1" * 101, value="2" * 101, description="3" * 101),
        SelectOption(label="1", value="2", description="3" * 101),
    ),
    min_values=2,
    max_values=36,
)
s.validate()
