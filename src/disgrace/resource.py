import io
import pathlib
from typing import TYPE_CHECKING

import attrs
import httpx

if TYPE_CHECKING:
    from disgrace._typeshed import Pathish

__all__ = ("FileResource", "MemoryResource", "WebResource")

type Resource = FileResource | WebResource | MemoryResource


@attrs.define
class FileResource:
    path: pathlib.Path = attrs.field(converter=pathlib.Path)
    filename: str = attrs.Factory(lambda s: s.path.name, takes_self=True)
    spoiler: bool = False

    if TYPE_CHECKING:

        def __init__(
            self, path: Pathish, *, filename: str = ..., spoiler: bool = False
        ) -> None: ...


@attrs.define
class WebResource:
    @staticmethod
    def filename_from_url(url: httpx.URL, /) -> str:
        return url.path.rsplit("/", 1)[-1]

    url: httpx.URL = attrs.field(converter=httpx.URL)
    filename: str = attrs.Factory(
        lambda s: WebResource.filename_from_url(s.url), takes_self=True
    )

    if TYPE_CHECKING:

        def __init__(self, url: str | httpx.URL, *, filename: str = ...) -> None: ...


@attrs.define
class MemoryResource:
    stream: io.BytesIO | io.StringIO
    filename: str


def with_spoiler[ResT: Resource](resource: ResT, /) -> ResT:
    if resource.filename.startswith("SPOILER_"):
        return resource
    return attrs.evolve(resource, filename="SPOILER_" + resource.filename)
