import datetime


def isoformat_utc(dt: datetime.datetime, /) -> str:
    return dt.astimezone(datetime.UTC).isoformat()
