import datetime
import enum
from collections import abc
from typing import ClassVar, Literal, Self

import msgspec

from disgrace.color import Color
from disgrace.limits import EmbedLimits
from disgrace.structs import embed
from disgrace.utils import isoformat_utc

from .._msgspec import BaseModel


class EditMode(enum.Enum):
    keep = enum.auto()
    remove = enum.auto()


class Footer(BaseModel, frozen=True, kw_only=True):
    text: str
    icon_url: str = ""
    proxy_icon_url: str = ""

    def to_struct(self) -> embed.RawEmbedFooter:
        return embed.RawEmbedFooter(
            text=self.text,
            icon_url=self.icon_url or msgspec.UNSET,
            proxy_icon_url=self.proxy_icon_url or msgspec.UNSET,
        )


class Media(BaseModel, frozen=True, kw_only=True):
    url: str
    proxy_url: str = ""

    def to_struct(self) -> embed.RawEmbedMedia:
        return embed.RawEmbedMedia(
            url=self.url,
            proxy_url=self.proxy_url or msgspec.UNSET,
        )


class Author(BaseModel, frozen=True, kw_only=True):
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


class Field(BaseModel, frozen=True, kw_only=True):
    name: str
    value: str
    inline: bool = True

    def to_struct(self) -> embed.RawEmbedField:
        return embed.RawEmbedField(
            name=self.name,
            value=self.value,
            inline=self.inline,
        )


class BuilderField(msgspec.Struct, kw_only=True):
    name: str
    value: str
    inline: bool = True

    def edit(
        self,
        *,
        name: str | Literal[EditMode.keep] = EditMode.keep,
        value: str | Literal[EditMode.keep] = EditMode.keep,
        inline: bool | Literal[EditMode.keep] = EditMode.keep,
    ) -> Self:
        if name is not EditMode.keep:
            self.name = name
        if value is not EditMode.keep:
            self.value = value
        if inline is not EditMode.keep:
            self.inline = inline
        return self

    def to_field(self) -> Field:
        return Field(name=self.name, value=self.value, inline=self.inline)


class EmbedBuilder(msgspec.Struct, kw_only=True):
    title: str = ""
    description: str = ""
    url: str = ""
    timestamp: datetime.datetime | None = None
    color: Color = msgspec.field(default_factory=lambda: Embed.default_color)
    footer: Footer | None = None
    image: Media | None = None
    thumbnail: Media | None = None
    author: Author | None = None
    fields: list[BuilderField] = []

    def edit(
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

    def edit_footer(
        self,
        text: str | Literal[EditMode.keep] = EditMode.keep,
        *,
        icon_url: str | EditMode = EditMode.keep,
        proxy_icon_url: str | EditMode = EditMode.keep,
    ) -> Self:
        if text is EditMode.keep:
            if self.footer is None:
                return self

            text = self.footer.text

        if icon_url is EditMode.remove:
            icon_url = ""
        elif icon_url is EditMode.keep:
            icon_url = self.footer.icon_url if self.footer is not None else ""

        if proxy_icon_url is EditMode.remove:
            proxy_icon_url = ""
        elif proxy_icon_url is EditMode.keep:
            proxy_icon_url = self.footer.proxy_icon_url if self.footer is not None else ""

        self.footer = Footer(text=text, icon_url=icon_url, proxy_icon_url=proxy_icon_url)
        return self

    def remove_footer(self) -> Self:
        self.footer = None
        return self

    def edit_image(
        self,
        url: str | Literal[EditMode.keep] = EditMode.keep,
        *,
        proxy_url: str | EditMode = EditMode.keep,
    ) -> Self:
        if url is EditMode.keep:
            if self.image is None:
                return self

            url = self.image.url

        if proxy_url is EditMode.remove:
            proxy_url = ""
        elif proxy_url is EditMode.keep:
            proxy_url = self.image.proxy_url if self.image is not None else ""

        self.image = Media(url=url, proxy_url=proxy_url)
        return self

    def remove_image(self) -> Self:
        self.image = None
        return self

    def edit_author(
        self,
        name: str | Literal[EditMode.keep] = EditMode.keep,
        *,
        url: str | EditMode = EditMode.keep,
        icon_url: str | EditMode = EditMode.keep,
        proxy_icon_url: str | EditMode = EditMode.keep,
    ) -> Self:
        if name is EditMode.keep:
            if self.author is None:
                return self

            name = self.author.name

        if url is EditMode.remove:
            url = ""
        elif url is EditMode.keep:
            url = self.author.url if self.author is not None else ""

        if icon_url is EditMode.remove:
            icon_url = ""
        elif icon_url is EditMode.keep:
            icon_url = self.author.icon_url if self.author is not None else ""

        if proxy_icon_url is EditMode.remove:
            proxy_icon_url = ""
        elif proxy_icon_url is EditMode.keep:
            proxy_icon_url = self.author.proxy_icon_url if self.author is not None else ""

        self.author = Author(
            name=name, url=url, icon_url=icon_url, proxy_icon_url=proxy_icon_url
        )
        return self

    def remove_author(self) -> Self:
        self.author = None
        return self

    def add_field(
        self,
        name: str,
        value: str,
        *,
        inline: bool = True,
    ) -> Self:
        self.fields.append(BuilderField(name=name, value=value, inline=inline))
        return self

    def build(self) -> "Embed":
        return Embed(
            title=self.title,
            description=self.description,
            url=self.url,
            timestamp=self.timestamp,
            color=self.color,
            footer=self.footer,
            image=self.image,
            thumbnail=self.thumbnail,
            author=self.author,
            fields=tuple(field.to_field() for field in self.fields),
        )


class Embed(BaseModel, frozen=True, kw_only=True):
    default_color: ClassVar[Color] = Color.none

    title: str = ""
    description: str = ""
    url: str = ""
    timestamp: datetime.datetime | None = None
    color: Color = msgspec.field(default_factory=lambda: Embed.default_color)
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
