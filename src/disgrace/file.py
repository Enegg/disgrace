import io
import os
import pathlib

import httpx
import msgspec

type StrPath = str | os.PathLike[str]


class FileResource(msgspec.Struct):
    path: StrPath
    filename: str = ""
    spoiler: bool = False

    def __post_init__(self) -> None:
        if not self.filename:
            self.filename = pathlib.PurePath(self.path).name


class WebResource(msgspec.Struct):
    url: str | httpx.URL
    filename: str = ""

    def __post_init__(self) -> None:
        if not self.filename:
            self.filename = httpx.URL(self.url).path.rsplit("/", 1)[-1]


class MemoryResource(msgspec.Struct):
    stream: io.BytesIO | io.StringIO
    filename: str
    spoiler: bool = False
