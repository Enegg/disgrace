from typing import NewType

SnowflakeId = NewType("SnowflakeId", int)
ChannelId = NewType("ChannelId", SnowflakeId)
GuildId = NewType("GuildId", SnowflakeId)
SkuId = NewType("SkuId", SnowflakeId)
UserId = NewType("UserId", SnowflakeId)
type MemberId = UserId
GuildEmojiId = NewType("GuildEmojiId", SnowflakeId)
AppEmojiId = NewType("AppEmojiId", SnowflakeId)
RoleId = NewType("RoleId", SnowflakeId)
MessageId = NewType("MessageId", SnowflakeId)
WebhookId = NewType("WebhookId", SnowflakeId)
ApplicationId = NewType("ApplicationId", SnowflakeId)
StickerId = NewType("StickerId", SnowflakeId)
StickerPackId = NewType("StickerPackId", SnowflakeId)
AttachmentId = NewType("AttachmentId", SnowflakeId)
