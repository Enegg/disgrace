from typing import Protocol

from disgrace import ids
from disgrace.asset import Asset

from .structural import Snowflake


class User(Snowflake[ids.UserId], Protocol):
    __slots__ = ()

    @property
    def username(self) -> str: ...
    @property
    def discriminator(self) -> str: ...
    @property
    def global_name(self) -> str | None: ...
    @property
    def avatar(self) -> Asset.StaticOrGifAsset | None: ...
    @property
    def bot(self) -> bool: ...
    @property
    def system(self) -> bool: ...


class WebhookUser(Snowflake[ids.WebhookId], Protocol):
    __slots__ = ()

    @property
    def username(self) -> str: ...
    @property
    def discriminator(self) -> str: ...
    @property
    def global_name(self) -> str | None: ...
    @property
    def avatar(self) -> Asset.StaticOrGifAsset | None: ...
    @property
    def bot(self) -> bool: ...
    @property
    def system(self) -> bool: ...
