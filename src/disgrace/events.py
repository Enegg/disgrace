import msgspec


class BasePayload(msgspec.Struct, tag_field="op"):
    d: object | None
    s: int | None
    t: str | None


class Dispatch(BasePayload, tag=0): ...


class Heartbeat(BasePayload, tag=1): ...


class Identify(BasePayload, tag=2): ...


class PresenceUpdate(BasePayload, tag=3): ...


class VoiceStateUpdate(BasePayload, tag=4): ...


class Resume(BasePayload, tag=6): ...


class Reconnect(BasePayload, tag=7): ...


class RequestGuildMembers(BasePayload, tag=8): ...


class InvalidSession(BasePayload, tag=9): ...


class Hello(BasePayload, tag=10): ...


class HeartbeatACK(BasePayload, tag=11): ...


class RequestSoundboardSounds(BasePayload, tag=31): ...
