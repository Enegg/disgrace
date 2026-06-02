from collections import abc
from typing import ClassVar, Final, Self, overload

import attrs


@attrs.define(eq=True)
class BaseFlags:
    value: int
    _DEFAULT_VALUE: ClassVar[int]
    _ALL_FLAGS_VALUE: ClassVar[int]
    _VALID_FLAG_NAMES: ClassVar[abc.Set[str]]

    def __init_subclass__(cls, inverted: bool = False) -> None:
        cls._ALL_FLAGS_VALUE = 0
        cls._VALID_FLAG_NAMES = set()

        for name, value in cls.__dict__.items():
            if isinstance(value, bit_value):
                cls._VALID_FLAG_NAMES.add(name)
                cls._ALL_FLAGS_VALUE |= value.bit

        cls._DEFAULT_VALUE = cls._ALL_FLAGS_VALUE if inverted else 0

    def __or__(self, other: Self, /) -> Self:
        return self.__class__(self.value | other.value)

    def __and__(self, other: Self, /) -> Self:
        return self.__class__(self.value & other.value)

    def __xor__(self, other: Self, /) -> Self:
        return self.__class__(self.value ^ other.value)

    def __invert__(self) -> Self:
        return self.__class__(
            (self.value ^ self._ALL_FLAGS_VALUE) & self._ALL_FLAGS_VALUE
        )

    def __index__(self) -> int:
        return self.value

    def __bool__(self) -> bool:
        return self.value != self._DEFAULT_VALUE

    @classmethod
    def none(cls) -> Self:
        return cls(cls._DEFAULT_VALUE)

    @classmethod
    def all(cls) -> Self:
        return cls(cls._ALL_FLAGS_VALUE)


@attrs.frozen
class bit_value:  # noqa: N801
    bit: Final[int]

    @overload
    def __get__[FlagsT: BaseFlags](
        self, obj: None, cls: abc.Callable[[int], FlagsT], /
    ) -> FlagsT: ...
    @overload
    def __get__(self, obj: BaseFlags, cls: type, /) -> bool: ...
    def __get__[FlagsT: BaseFlags](
        self, obj: FlagsT | None, cls: abc.Callable[[int], FlagsT], /
    ) -> bool | FlagsT:
        if obj is None:
            return cls(self.bit)
        return obj.value & self.bit != 0

    def __set__(self, obj: BaseFlags, value: bool, /) -> None:
        if value:
            obj.value |= self.bit
        else:
            obj.value &= ~self.bit


@attrs.define(eq=True)
class Permissions(BaseFlags):
    def __init__(self, value: int = 0) -> None:
        super().__init__(value)

    create_instant_invite = bit_value(1 << 0)
    """Allows creation of instant invites."""
    kick_members = bit_value(1 << 1)
    """Allows kicking members."""
    ban_members = bit_value(1 << 2)
    """Allows banning members."""
    administrator = bit_value(1 << 3)
    """Allows all permissions and bypasses channel permission overwrites."""
    manage_channels = bit_value(1 << 4)
    """Allows management and editing of channels."""
    manage_guild = bit_value(1 << 5)
    """Allows management and editing of the guild."""
    add_reactions = bit_value(1 << 6)
    """Allows for adding new reactions to messages. This permission does not apply
    to reacting with an existing reaction on a message."""
    view_audit_log = bit_value(1 << 7)
    """Allows for viewing of audit logs."""
    priority_speaker = bit_value(1 << 8)
    """Allows for using priority speaker in a voice channel."""
    stream = bit_value(1 << 9)
    """Allows the user to go live."""
    view_channel = bit_value(1 << 10)
    """Allows guild members to view a channel, which includes reading messages
    in text channels and joining voice channels."""
    send_messages = bit_value(1 << 11)
    """Allows for sending messages in a channel and creating threads in a forum
    (does not allow sending messages in threads)."""
    send_tts_messages = bit_value(1 << 12)
    """Allows for sending of `/tts` messages."""
    manage_messages = bit_value(1 << 13)
    """Allows for deletion of other users' messages."""
    embed_links = bit_value(1 << 14)
    """Links sent by users with this permission will be auto-embedded."""
    attach_files = bit_value(1 << 15)
    """Allows for uploading images and files."""
    read_message_history = bit_value(1 << 16)
    """Allows for reading of message history."""
    mention_everyone = bit_value(1 << 17)
    external_emojis = bit_value(1 << 18)
    view_guild_insights = bit_value(1 << 19)
    connect = bit_value(1 << 20)
    speak = bit_value(1 << 21)
    mute_members = bit_value(1 << 22)
    deafen_members = bit_value(1 << 23)
    move_members = bit_value(1 << 24)
    use_voice_activation = bit_value(1 << 25)
    change_nickname = bit_value(1 << 26)
    manage_nicknames = bit_value(1 << 27)
    manage_roles = bit_value(1 << 28)
    manage_webhooks = bit_value(1 << 29)
    manage_guild_expressions = bit_value(1 << 30)
    use_application_commands = bit_value(1 << 31)
    request_to_speak = bit_value(1 << 32)
    manage_events = bit_value(1 << 33)
    manage_threads = bit_value(1 << 34)
    create_public_threads = bit_value(1 << 35)
    create_private_threads = bit_value(1 << 36)
    external_stickers = bit_value(1 << 37)
    send_messages_in_threads = bit_value(1 << 38)
    use_embedded_activities = bit_value(1 << 39)
    moderate_members = bit_value(1 << 40)
    view_creator_monetization_analytics = bit_value(1 << 41)
    use_soundboard = bit_value(1 << 42)
    create_guild_expressions = bit_value(1 << 43)
    create_events = bit_value(1 << 44)
    use_external_sounds = bit_value(1 << 45)
    send_voice_messages = bit_value(1 << 46)
    # gap
    send_polls = bit_value(1 << 49)
    use_external_apps = bit_value(1 << 50)
