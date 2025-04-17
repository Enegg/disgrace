import enum
from collections import abc
from typing import Any, ClassVar

import attrs


@attrs.define
class Route:
    BASE: ClassVar[str] = "https://discord.com/api/v10"

    class Method(enum.StrEnum):
        GET = "GET"
        PUT = "PUT"
        POST = "POST"
        PATCH = "PATCH"
        DELETE = "DELETE"

    method: Method
    path: str


async def request(route: Route, *, files: abc.Sequence[object] = ()) -> Any: ...
