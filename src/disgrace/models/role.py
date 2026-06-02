import msgspec

from disgrace import ids
from disgrace._msgspec import BaseModel
from disgrace.asset import Asset
from disgrace.color import Color

from .common import created_at
from .emoji import UnicodeEmoji
from .permissions import Permissions


class Role(BaseModel, frozen=True, kw_only=True):
    id: ids.RoleId
    name: str
    color: Color | None = None
    icon: Asset.StaticAsset | None = None
    emoji: UnicodeEmoji | None = None
    position: int = 0
    # TODO: this class is frozen. Permissions is mutable. Oops!
    permissions: Permissions = msgspec.field(default_factory=Permissions)
    hoist: bool = False
    managed: bool = False
    mentionable: bool = False
    tags: object = None
    flags: int = 0

    created_at = created_at
