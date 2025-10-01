from collections import abc
from typing import Protocol

from disgrace import ui
from disgrace.allowed_mentions import AllowedMentions
from disgrace.flags import MessageFlags
from disgrace.models.embed import Embed
from disgrace.resource import FileResource

type Sticker = object  # TODO: Stickers
type Poll = object  # TODO: Polls


class Messageable(Protocol):
    __slots__ = ()

    def send(
        self,
        content: str | None = None,
        *,
        embeds: Embed | abc.Sequence[Embed] = (),
        files: FileResource | abc.Sequence[FileResource] = (),
        stickers: abc.Sequence[Sticker] = (),
        flags: MessageFlags = MessageFlags.none,
        allowed_mentions: AllowedMentions | None = None,
        components: ui.MessageComponents = (),
        poll: Poll | None = None,
    ) -> abc.Awaitable[None]: ...  # TODO


class MessageableV2(Protocol):
    __slots__ = ()

    def send_components(
        self,
        components: ui.TopLevelMessageComponent,
        *,
        allowed_mentions: AllowedMentions | None = None,
    ) -> abc.Awaitable[None]: ...
