import io
import pathlib

import httpx
import msgspec

from disgrace._typeshed import Pathish

__all__ = ("FileResource", "MemoryResource", "WebResource")

type Resource = FileResource | WebResource | MemoryResource


class FileResource(msgspec.Struct, kw_only=True):
    path: Pathish
    filename: str = ""
    spoiler: bool = False

    def __post_init__(self) -> None:
        if not self.filename:
            self.filename = pathlib.PurePath(self.path).name


class WebResource(msgspec.Struct, kw_only=True):
    url: str | httpx.URL
    filename: str = ""

    def __post_init__(self) -> None:
        if not self.filename:
            self.filename = httpx.URL(self.url).path.rsplit("/", 1)[-1]


class MemoryResource(msgspec.Struct):
    stream: io.BytesIO | io.StringIO
    filename: str
    spoiler: bool = False
