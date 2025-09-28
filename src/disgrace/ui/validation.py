from collections import abc
from typing import Self, override

import attrs

from disgrace.limits import ComponentLimits
from disgrace.ui import (
    ActionButton,
    ActionRow,
    AnyButton,
    AnySelect,
    ChannelSelect,
    Container,
    File,
    Label,
    LinkButton,
    MediaGallery,
    MentionableSelect,
    PremiumButton,
    RoleSelect,
    Section,
    SelectOption,
    Separator,
    StringSelect,
    TextDisplay,
    TextInput,
    Thumbnail,
    TopLevelMessageComponent,
    UserSelect,
)
from disgrace.utils import Range

type AnyMessageComponent = TopLevelMessageComponent | AnyButton | AnySelect | Thumbnail
type AnyModalComponent = TextInput | Label


@attrs.define
class Diagnostic:
    path: tuple[str | int, ...]
    msg: str

    @override
    def __str__(self) -> str:
        path = ["at $"]
        for piece in self.path:
            if isinstance(piece, str):
                path.append(f".{piece}")
            else:
                path.append(f"[{piece}]")
        return f"{''.join(path)}:\n    {self.msg}"


@attrs.define
class ValidationContext:
    path: tuple[str | int, ...] = ()
    diagnostics: abc.MutableSequence[Diagnostic] = attrs.Factory(list[Diagnostic])

    @override
    def __str__(self) -> str:
        return "\n".join(map(str, self.diagnostics))

    def add(self, field: str, msg: str) -> None:
        self.diagnostics.append(Diagnostic((*self.path, field), msg))

    def derrive(self, *path: str | int) -> Self:
        return type(self)((*self.path, *path), self.diagnostics)

    def enumerate[T](
        self, it: abc.Iterable[T], /, *path: int | str
    ) -> abc.Iterable[tuple[Self, T]]:
        for i, val in enumerate(it):
            yield self.derrive(*path, i), val

    def check_length_oob(
        self,
        component_name: str,
        field: str,
        value: abc.Sized,
        length: Range,
    ) -> None:
        if length.min == 0 and len(value) > length.max:
            self.add(
                field,
                f"len({component_name}.{field}) > {length.max} (= {len(value)})",
            )

        elif len(value) not in length:
            self.add(
                field,
                f"len({component_name}.{field}) ∉ {length} (= {len(value)})",
            )

    def check_select_options(
        self,
        select_name: str,
        options_field_name: str,
        options: abc.Sized | int,
        min_values: int,
        max_values: int,
        can_be_empty: bool = False,
    ) -> None:
        min_is_ok = min_values in ComponentLimits.select_min_max_values
        max_is_ok = max_values in ComponentLimits.select_min_max_values
        array_limit = (
            ComponentLimits.select_min_max_values
            if can_be_empty
            else ComponentLimits.select_options
        )
        option_count = options if isinstance(options, int) else len(options)

        if not min_is_ok:
            self.add(
                "min_values",
                f"{select_name}.min_values ∉ {ComponentLimits.select_min_max_values} (= {min_values})",  # noqa: E501
            )
        if not max_is_ok:
            self.add(
                "max_values",
                f"{select_name}.max_values ∉ {ComponentLimits.select_min_max_values} (= {max_values})",  # noqa: E501
            )
        if option_count not in array_limit:
            self.add(
                options_field_name,
                f"len({select_name}.{options_field_name}) ∉ {array_limit} (= {option_count})",  # noqa: E501
            )
        if max_values < min_values:
            self.add(
                "max_values",
                f"{select_name}.max_values < {select_name}.min_values ({max_values} < {min_values})",  # noqa: E501
            )

        elif can_be_empty and option_count == 0:
            pass

        elif not min_values <= option_count <= max_values:
            self.add(
                options_field_name,
                f"len({select_name}.{options_field_name}) ∉ {min_values}..{max_values} (= {option_count}) (min_values..max_values)",  # noqa: E501
            )

    def check_text_input(
        self,
        component_name: str,
        value: str,
        min_length: int,
        max_length: int,
    ) -> None:
        min_length_range = Range(0, ComponentLimits.text_input_value)
        max_length_range = Range(1, ComponentLimits.text_input_value)
        min_is_ok = min_length in min_length_range
        max_is_ok = max_length in max_length_range

        if not min_is_ok:
            self.add(
                "min_length",
                f"{component_name}.min_length ∉ {min_length_range} (= {min_length})",
            )
        if not max_is_ok:
            self.add(
                "max_length",
                f"{component_name}.max_length ∉ {max_length_range} (= {max_length})",
            )
        if len(value) not in min_length_range:
            self.add(
                "value",
                f"len({component_name}.value) ∉ {min_length_range} (= {len(value)})",
            )
        if max_length < min_length:
            self.add(
                "max_length",
                f"{component_name}.max_length < {component_name}.min_length ({max_length} < {min_length})",  # noqa: E501
            )

        elif not min_length <= len(value) <= max_length:
            self.add(
                "value",
                f"len({component_name}.value) ∉ {min_length}..{max_length} (= {len(value)}) (min_length..max_length)",  # noqa: E501
            )


def validate_components(
    components: AnyMessageComponent, /
) -> abc.MutableSequence[Diagnostic]:
    ctx = ValidationContext()
    _traverse_components(components, ctx)
    return ctx.diagnostics


def _traverse_components(component: AnyMessageComponent, ctx: ValidationContext) -> None:
    match component:
        case ActionRow():
            validate_action_row(component, ctx)

            for subctx, child in ctx.enumerate(component.components, "components"):
                _traverse_components(child, subctx)

        case ActionButton():
            validate_action_button(component, ctx)

        case LinkButton():
            validate_link_button(component, ctx)

        case PremiumButton():
            ...

        case StringSelect():
            validate_string_select(component, ctx)

        case UserSelect():
            validate_user_select(component, ctx)

        case RoleSelect():
            validate_role_select(component, ctx)

        case MentionableSelect():
            validate_mentionable_select(component, ctx)

        case ChannelSelect():
            validate_channel_select(component, ctx)

        case Section():
            validate_section(component, ctx)

            for subctx, child in ctx.enumerate(component.components, "components"):
                _traverse_components(child, subctx)
            _traverse_components(component.accessory, ctx.derrive("accessory"))

        case TextDisplay():
            ...

        case Thumbnail():
            validate_thumbnail(component, ctx)

        case MediaGallery():
            validate_media_gallery(component, ctx)

        case File():
            ...

        case Separator():
            ...

        case Container():
            for subctx, child in ctx.enumerate(component.components, "components"):
                _traverse_components(child, subctx)


def validate_action_row(action_row: ActionRow, v: ValidationContext, /) -> None:
    v.check_length_oob(
        ActionRow.__name__,
        "components",
        action_row.components,
        Range(0, ComponentLimits.action_row_buttons),
    )


def validate_action_button(button: ActionButton, v: ValidationContext, /) -> None:
    v.check_length_oob(
        "Button",
        "custom_id",
        button.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        "Button",
        "label",
        button.label,
        Range(0, ComponentLimits.button_label),
    )


def validate_link_button(button: LinkButton, v: ValidationContext, /) -> None:
    v.check_length_oob(
        "Button",
        "label",
        button.label,
        Range(0, ComponentLimits.button_label),
    )


def validate_string_select(select: StringSelect, v: ValidationContext) -> None:
    v.check_length_oob(
        StringSelect.__name__,
        "custom_id",
        select.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        StringSelect.__name__,
        "placeholder",
        select.placeholder,
        Range(0, ComponentLimits.select_placeholder),
    )
    v.check_select_options(
        StringSelect.__name__,
        "options",
        select.options,
        select.min_values,
        select.max_values,
    )

    for new_v, option in v.enumerate(select.options, "options"):
        new_v.check_length_oob(
            SelectOption.__name__,
            "label",
            option.label,
            Range(0, ComponentLimits.select_option_label),
        )
        new_v.check_length_oob(
            SelectOption.__name__,
            "value",
            option.value,
            Range(0, ComponentLimits.select_option_value),
        )
        new_v.check_length_oob(
            SelectOption.__name__,
            "description",
            option.description,
            Range(0, ComponentLimits.select_option_description),
        )


def validate_text_input(input: TextInput, v: ValidationContext) -> None:
    v.check_length_oob(
        TextInput.__name__,
        "custom_id",
        input.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        TextInput.__name__,
        "placeholder",
        input.placeholder,
        Range(0, ComponentLimits.text_input_placeholder),
    )
    v.check_text_input(
        TextInput.__name__, input.value, input.min_length, input.max_length
    )


def validate_user_select(select: UserSelect, v: ValidationContext) -> None:
    v.check_length_oob(
        UserSelect.__name__,
        "custom_id",
        select.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        UserSelect.__name__,
        "placeholder",
        select.placeholder,
        Range(0, ComponentLimits.select_placeholder),
    )
    v.check_select_options(
        UserSelect.__name__,
        "default_users",
        select.default_users,
        select.min_values,
        select.max_values,
        can_be_empty=True,
    )


def validate_role_select(select: RoleSelect, v: ValidationContext) -> None:
    v.check_length_oob(
        RoleSelect.__name__,
        "custom_id",
        select.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        RoleSelect.__name__,
        "placeholder",
        select.placeholder,
        Range(0, ComponentLimits.select_placeholder),
    )
    v.check_select_options(
        RoleSelect.__name__,
        "default_roles",
        select.default_roles,
        select.min_values,
        select.max_values,
        can_be_empty=True,
    )


def validate_mentionable_select(select: MentionableSelect, v: ValidationContext) -> None:
    v.check_length_oob(
        UserSelect.__name__,
        "custom_id",
        select.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        UserSelect.__name__,
        "placeholder",
        select.placeholder,
        Range(0, ComponentLimits.select_placeholder),
    )
    v.check_select_options(
        UserSelect.__name__,
        "{default_users,default_roles}",
        len(select.default_users) + len(select.default_roles),
        select.min_values,
        select.max_values,
        can_be_empty=True,
    )


def validate_channel_select(select: ChannelSelect, v: ValidationContext) -> None:
    v.check_length_oob(
        UserSelect.__name__,
        "custom_id",
        select.custom_id,
        Range(0, ComponentLimits.custom_id),
    )
    v.check_length_oob(
        UserSelect.__name__,
        "placeholder",
        select.placeholder,
        Range(0, ComponentLimits.select_placeholder),
    )
    v.check_select_options(
        UserSelect.__name__,
        "default_channels",
        select.default_channels,
        select.min_values,
        select.max_values,
        can_be_empty=True,
    )


def validate_section(section: Section, v: ValidationContext) -> None:
    v.check_length_oob(
        Section.__name__,
        "components",
        section.components,
        ComponentLimits.section_components_range,
    )


def validate_thumbnail(thumbnail: Thumbnail, v: ValidationContext) -> None:
    v.check_length_oob(
        Thumbnail.__name__,
        "description",
        thumbnail.description,
        Range(0, ComponentLimits.media_description),
    )


def validate_media_gallery(gallery: MediaGallery, v: ValidationContext) -> None:
    v.check_length_oob(
        MediaGallery.__name__,
        "items",
        gallery.items,
        ComponentLimits.gallery_items,
    )
