import datetime
import enum
from collections import abc
from typing import ClassVar, Self

import msgspec

from disgrace.color import Color
from disgrace.limits import EmbedLimits
from disgrace.structs import embed
from disgrace.utils import isoformat_utc


class EditMode(enum.Enum):
    keep = enum.auto()
    remove = enum.auto()


class Footer(msgspec.Struct, frozen=True, kw_only=True):
    text: str
    icon_url: str = ""
    proxy_icon_url: str = ""

    def to_struct(self) -> embed.RawEmbedFooter:
        return embed.RawEmbedFooter(
            text=self.text,
            icon_url=self.icon_url or msgspec.UNSET,
            proxy_icon_url=self.proxy_icon_url or msgspec.UNSET,
        )


class Media(msgspec.Struct, frozen=True, kw_only=True):
    url: str
    proxy_url: str = ""

    def to_struct(self) -> embed.RawEmbedMedia:
        return embed.RawEmbedMedia(
            url=self.url,
            proxy_url=self.proxy_url or msgspec.UNSET,
        )


class Author(msgspec.Struct, frozen=True, kw_only=True):
    name: str
    url: str = ""
    icon_url: str = ""
    proxy_icon_url: str = ""

    def to_struct(self) -> embed.RawEmbedAuthor:
        return embed.RawEmbedAuthor(
            name=self.name,
            url=self.url or msgspec.UNSET,
            icon_url=self.icon_url or msgspec.UNSET,
            proxy_icon_url=self.proxy_icon_url or msgspec.UNSET,
        )


class Field(msgspec.Struct, frozen=True, kw_only=True):
    name: str
    value: str
    inline: bool = True

    def to_struct(self) -> embed.RawEmbedField:
        return embed.RawEmbedField(
            name=self.name,
            value=self.value,
            inline=self.inline,
        )


class EmbedBuilder(msgspec.Struct, kw_only=True):
    default_color: ClassVar[Color] = Color.none

    title: str = ""
    description: str = ""
    url: str = ""
    timestamp: datetime.datetime | None = None
    color: Color = Color.none
    footer: Footer | None = None
    image: Media | None = None
    thumbnail: Media | None = None
    author: Author | None = None
    fields: list[Field] = []

    def set_title(
        self,
        title: str | EditMode = EditMode.keep,
        description: str | EditMode = EditMode.keep,
        url: str | EditMode = EditMode.keep,
        timestamp: datetime.datetime | EditMode = EditMode.keep,
        color: Color | EditMode = EditMode.keep,
    ) -> Self:
        if title is EditMode.remove:
            self.title = ""
        elif title is not EditMode.keep:
            self.title = title

        if description is EditMode.remove:
            self.description = ""
        elif description is not EditMode.keep:
            self.description = description

        if url is EditMode.remove:
            self.url = ""
        elif url is not EditMode.keep:
            self.url = url

        if timestamp is EditMode.remove:
            self.timestamp = None
        elif timestamp is not EditMode.keep:
            self.timestamp = timestamp

        if color is EditMode.remove:
            self.color = Color.none
        elif color is not EditMode.keep:
            self.color = color

        return self

    # TODO
    def set_footer(
        self, text: str, *, icon_url: str = "", proxy_icon_url: str = ""
    ) -> Self: ...
    def set_image(self, url: str, *, proxy_url: str = "") -> Self: ...
    def set_author(
        self, name: str, *, url: str = "", icon_url: str = "", proxy_icon_url: str = ""
    ) -> Self: ...
    def add_field(self, name: str, value: str, *, inline: bool = True) -> Self: ...
    def build(self) -> "Embed":
        return Embed(
            title=self.title,
            description=self.description,
            url=self.url,
            timestamp=self.timestamp,
            color=self.color or self.default_color,
            footer=self.footer,
            image=self.image,
            thumbnail=self.thumbnail,
            author=self.author,
            fields=tuple(self.fields),
        )


class Embed(msgspec.Struct, frozen=True, kw_only=True):
    title: str = ""
    description: str = ""
    url: str = ""
    timestamp: datetime.datetime | None = None
    color: Color = msgspec.field(default_factory=lambda: EmbedBuilder.default_color)
    footer: Footer | None = None
    image: Media | None = None
    thumbnail: Media | None = None
    author: Author | None = None
    fields: abc.Sequence[Field] = ()

    def to_struct(self) -> embed.RawEmbed:
        if __debug__:
            self.validate()
        return embed.RawEmbed(
            title=self.title or msgspec.UNSET,
            description=self.description or msgspec.UNSET,
            url=self.url or msgspec.UNSET,
            timestamp=msgspec.UNSET
            if self.timestamp is None
            else isoformat_utc(self.timestamp),
            color=self.color.value or msgspec.UNSET,
            footer=msgspec.UNSET if self.footer is None else self.footer.to_struct(),
            image=msgspec.UNSET if self.image is None else self.image.to_struct(),
            thumbnail=msgspec.UNSET
            if self.thumbnail is None
            else self.thumbnail.to_struct(),
            author=msgspec.UNSET if self.author is None else self.author.to_struct(),
            fields=[field.to_struct() for field in self.fields],
        )

    def validate(self) -> None:
        fields: list[str] = []

        footer_text = 0 if self.footer is None else len(self.footer.text)
        author_name = 0 if self.author is None else len(self.author.name)

        if len(self.title) > EmbedLimits.title:
            fields.append(f"{len(self.title)=} (> {EmbedLimits.title})")
        if len(self.description) > EmbedLimits.description:
            fields.append(f"{len(self.description)=} (> {EmbedLimits.description})")
        if self.footer is not None and footer_text > EmbedLimits.footer_text:
            fields.append(f"{len(self.footer.text)=} (> {EmbedLimits.footer_text})")
        if self.author is not None and author_name > EmbedLimits.author_name:
            fields.append(f"{len(self.author.name)=} (> {EmbedLimits.author_name})")

        total = len(self.title) + len(self.description) + footer_text + author_name
        for i, field in enumerate(self.fields):
            field_name, field_value = len(field.name), len(field.value)
            total += field_name + field_value
            if field_name > EmbedLimits.field_name:
                fields.append(
                    f"len(self.fields[{i}].name)={field_name} (> {EmbedLimits.field_name})"  # noqa: E501
                )
            if field_value > EmbedLimits.field_value:
                fields.append(
                    f"len(self.fields[{i}].value)={field_value} (> {EmbedLimits.field_value})"  # noqa: E501
                )
        if total > EmbedLimits.total:
            fields.append(f"total={total} (> {EmbedLimits.total})")

        if fields:
            text = f"Embed exceeds size limits:\n{'\n'.join(fields)}"
            raise ValueError(text)
