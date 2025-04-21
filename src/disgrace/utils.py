import datetime
from typing import Final

from disgrace.ids import SnowflakeId

DISCORD_EPOCH: Final = 1_420_070_400_000


def isoformat_utc(dt: datetime.datetime, /) -> str:
    return dt.astimezone(datetime.UTC).isoformat()


def snowflake_time(id: SnowflakeId, /) -> datetime.datetime:
    timestamp_ms = (id >> 22) + DISCORD_EPOCH
    return datetime.datetime.fromtimestamp(timestamp_ms / 1000, tz=datetime.UTC)
