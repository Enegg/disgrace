import attrs


@attrs.define
class Client:
    async def login(self) -> None: ...

