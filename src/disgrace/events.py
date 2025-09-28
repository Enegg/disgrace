from typing import Any, ClassVar, Literal

import msgspec


class BasePayload(msgspec.Struct, tag_field="op"):
    op: ClassVar[Any | int]
    d: object | None
    s: int | None
    t: str | None


class Dispatch(BasePayload, tag=0):
    op: ClassVar[Literal[0]]


class Heartbeat(BasePayload, tag=1):
    op: ClassVar[Literal[1]]


class Identify(BasePayload, tag=2):
    op: ClassVar[Literal[2]]


class PresenceUpdate(BasePayload, tag=3):
    op: ClassVar[Literal[3]]


class VoiceStateUpdate(BasePayload, tag=4):
    op: ClassVar[Literal[4]]


class Resume(BasePayload, tag=6):
    op: ClassVar[Literal[6]]


class Reconnect(BasePayload, tag=7):
    op: ClassVar[Literal[7]]


class RequestGuildMembers(BasePayload, tag=8):
    op: ClassVar[Literal[8]]


class InvalidSession(BasePayload, tag=9):
    op: ClassVar[Literal[9]]


class Hello(BasePayload, tag=10):
    op: ClassVar[Literal[10]]

class HeartbeatACK(BasePayload, tag=11):
    op: ClassVar[Literal[11]]


class RequestSoundboardSounds(BasePayload, tag=31):
    op: ClassVar[Literal[31]]
