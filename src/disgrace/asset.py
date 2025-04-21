from typing import TYPE_CHECKING, Literal, Self, cast as cast_type

import attrs

from disgrace import ids
from disgrace.urls import ALT_CDN, CDN

type AssetSize = Literal[16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
type Png = Literal["png"]
type Gif = Literal["gif"]
type Lottie = Literal["json"]
type StaticFormat = Literal["webp", "jpeg", "jpg"] | Png
type StaticOrGif = StaticFormat | Gif


@attrs.frozen
class Asset[FmtT: StaticOrGif | Lottie]:
    url: str
    format: FmtT = cast_type("FmtT", "png")  # noqa: RUF009
    size: AssetSize = 4096

    if TYPE_CHECKING:

        def __init__(
            self, url: str, format: FmtT = "png", size: AssetSize = 4096
        ) -> None: ...

    def with_format(self, format: FmtT) -> Self:
        return attrs.evolve(self, format=format)

    def with_size(self, size: AssetSize) -> Self:
        return attrs.evolve(self, size=size)

    @classmethod
    def _from_icon(
        cls,
        type: Literal["app", "team", "role"],
        object_id: ids.SnowflakeId,
        icon_hash: str,
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/{type}-icons/{object_id}/{icon_hash}")

    @classmethod
    def from_emoji(
        cls, emoji_id: ids.GuildEmojiId | ids.AppEmojiId, animated: bool = False
    ) -> "Asset[StaticOrGif]":
        fmt = "gif" if animated else "png"
        return Asset(url=f"{CDN}/emojis/{emoji_id}", format=fmt)

    @classmethod
    def guild_icon(cls, guild_id: ids.GuildId, guild_icon: str) -> "Asset[StaticOrGif]":
        fmt = "gif" if guild_icon.startswith("a_") else "png"
        return Asset[StaticOrGif](url=f"{CDN}/icons/{guild_id}/{guild_icon}", format=fmt)

    @classmethod
    def guild_splash(cls, guild_id: ids.GuildId, splash: str) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/splashes/{guild_id}/{splash}")

    @classmethod
    def guild_discovery_splash(
        cls, guild_id: ids.GuildId, splash: str
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/discovery-splashes/{guild_id}/{splash}")

    @classmethod
    def guild_banner(cls, guild_id: ids.GuildId, banner: str) -> "Asset[StaticOrGif]":
        fmt = "gif" if banner.startswith("a_") else "png"
        return Asset(url=f"{CDN}/banners/{guild_id}/{banner}", format=fmt)

    @classmethod
    def user_banner(cls, user_id: ids.UserId, banner: str) -> "Asset[StaticOrGif]":
        fmt = "gif" if banner.startswith("a_") else "png"
        return Asset(url=f"{CDN}/banners/{user_id}/{banner}", format=fmt)

    @classmethod
    def default_user_avatar(cls, index: int) -> "Asset[Png]":
        return Asset[Png](url=f"{CDN}/embed/avatars/{index}")

    @classmethod
    def user_avatar(cls, user_id: ids.UserId, avatar: str) -> "Asset[StaticOrGif]":
        fmt = "gif" if avatar.startswith("a_") else "png"
        return Asset(url=f"{CDN}/avatars/{user_id}/{avatar}", format=fmt)

    @classmethod
    def guild_member_avatar(
        cls, guild_id: ids.GuildId, user_id: ids.UserId, avatar: str
    ) -> "Asset[StaticOrGif]":
        fmt = "gif" if avatar.startswith("a_") else "png"
        return Asset(
            url=f"{CDN}/guilds/{guild_id}/users/{user_id}/avatars/{avatar}", format=fmt
        )

    @classmethod
    def avatar_decoration(cls, asset: str) -> "Asset[Png]":
        return Asset(url=f"{CDN}/avatar-decoration-presets/{asset}")

    @classmethod
    def application_icon(
        cls, app_id: ids.ApplicationId, icon: str
    ) -> "Asset[StaticFormat]":
        return cls._from_icon("app", app_id, icon)

    @classmethod
    def application_cover(
        cls, app_id: ids.ApplicationId, cover: str
    ) -> "Asset[StaticFormat]":
        return cls._from_icon("app", app_id, cover)

    @classmethod
    def application_asset(
        cls, app_id: ids.ApplicationId, asset_id: str
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/app-assets/{app_id}/{asset_id}")

    @classmethod
    def achievement_icon(
        cls, app_id: ids.ApplicationId, achievement_id: str, icon: str
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](
            url=f"{CDN}/app-assets/{app_id}/achievements/{achievement_id}/icons/{icon}"
        )

    @classmethod
    def store_page_asset(
        cls, app_id: ids.ApplicationId, asset_id: str
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/app-assets/{app_id}/store/{asset_id}")

    @classmethod
    def sticker_pack_banner(cls, asset_id: str) -> "Asset[StaticFormat]":
        # hardcoded ID. Fun!
        return Asset[StaticFormat](
            url=f"{CDN}/app-assets/710982414301790216/store/{asset_id}"
        )

    @classmethod
    def team_icon(cls, team_id: ids.SnowflakeId, icon: str) -> "Asset[StaticFormat]":
        return cls._from_icon("team", team_id, icon)

    @classmethod
    def sticker_static(cls, sticker_id: ids.StickerId) -> "Asset[Png]":
        return Asset(url=f"{CDN}/stickers/{sticker_id}", format="png")

    @classmethod
    def sticker_lottie(cls, sticker_id: ids.StickerId) -> "Asset[Lottie]":
        return Asset(url=f"{CDN}/stickers/{sticker_id}", format="json")

    @classmethod
    def sticker_gif(cls, sticker_id: ids.StickerId) -> "Asset[Gif]":
        return Asset(url=f"{ALT_CDN}/stickers/{sticker_id}", format="gif")

    @classmethod
    def role_icon(cls, role_id: ids.RoleId, icon: str) -> "Asset[StaticFormat]":
        return cls._from_icon("role", role_id, icon)

    @classmethod
    def guild_scheduled_event_cover(
        cls, event_id: ids.SnowflakeId, cover: str
    ) -> "Asset[StaticFormat]":
        return Asset[StaticFormat](url=f"{CDN}/guild-events/{event_id}/{cover}")

    @classmethod
    def guild_member_banner(
        cls, guild_id: ids.GuildId, user_id: ids.UserId, banner: str
    ) -> "Asset[StaticOrGif]":
        fmt = "gif" if banner.startswith("a_") else "png"
        return Asset(
            url=f"{CDN}/guilds/{guild_id}/users/{user_id}/banners/{banner}", format=fmt
        )
