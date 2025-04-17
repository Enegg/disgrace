from collections import abc
from typing import Protocol

from disgrace.file import FileResource
from disgrace.flags import MessageFlags
from disgrace.models.embed import Embed

type Component = object  # TODO: Components
type Sticker = object  # TODO: Stickers
type Poll = object  # TODO: Polls


class Messageable(Protocol):
    def send(
        self,
        content: str | None = None,
        *,
        embeds: Embed | abc.Sequence[Embed] = (),
        files: FileResource | abc.Sequence[FileResource] = (),
        stickers: abc.Sequence[Sticker] = (),
        flags: MessageFlags = MessageFlags.none,
        allowed_mentions: ... = ...,
        components: abc.Sequence[Component] = (),
        poll: Poll | None = None,
    ) -> abc.Awaitable[None]: ...  # TODO
