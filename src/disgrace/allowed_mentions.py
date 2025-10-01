from collections import abc
from typing import Literal, Self

import msgspec

import disgrace.abc
from disgrace import ids
from disgrace.models.common import cast_str_id
from disgrace.structs import raw_ids

__all__ = ("AllowedMentions",)


class AllowedMentions(msgspec.Struct, kw_only=True, omit_defaults=True):
    type LiteralParseValue = Literal["roles", "users", "everyone"]

    parse: abc.Collection[LiteralParseValue] | msgspec.UnsetType = msgspec.UNSET
    users: abc.Collection[raw_ids.UserId] = ()
    roles: abc.Collection[raw_ids.RoleId] = ()
    replied_user: bool = False

    @classmethod
    def none(cls) -> Self:
        return cls(parse=())

    @classmethod
    def parsed(
        cls, *, users: bool = False, roles: bool = False, everyone: bool = False
    ) -> Self:
        parse: list[AllowedMentions.LiteralParseValue] = []
        if users:
            parse.append("users")
        if roles:
            parse.append("roles")
        if everyone:
            parse.append("everyone")
        return cls(parse=parse)

    @classmethod
    def snowflakes(
        cls,
        users: abc.Iterable[disgrace.abc.Snowflake[ids.UserId]] = (),
        roles: abc.Iterable[disgrace.abc.Snowflake[ids.RoleId]] = (),
        replies: bool = False,
    ) -> Self:
        return cls(
            users=tuple(cast_str_id(flake.id) for flake in users),
            roles=tuple(cast_str_id(flake.id) for flake in roles),
            replied_user=replies,
        )
