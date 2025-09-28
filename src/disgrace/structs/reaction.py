from collections import abc

import msgspec

from .emoji import PartialEmoji


class RawReactionCountDetails(msgspec.Struct, kw_only=True):
    burst: int
    normal: int


class RawReaction(msgspec.Struct, kw_only=True):
    count: int
    count_details: RawReactionCountDetails
    me: bool
    me_burst: bool
    emoji: PartialEmoji
    burst_colors: abc.Sequence[int]
