"""Collection of functions related to discord flavored markdown formatting."""

import datetime
import enum
from typing import Literal, override

import disgrace.abc
from disgrace.ids import RoleId


def hyperlink(text: str, url: str) -> str:
    """Format text into a hyperlink."""
    return f"[{text}]({url})"


def codeblock(text: str, lang: str = "") -> str:
    """Format text into a codeblock."""
    return f"```{lang}\n{text}```"


def format_dt(
    dt: datetime.datetime | float | int,
    /,
    style: Literal["f", "F", "d", "D", "t", "T", "R"] = "f",
) -> str:
    R"""Format a `datetime.datetime`, `int` or `float` for presentation within Discord.

    The exact output depends on the user's locale setting in the client.
    The example output below is using the ``en-GB`` locale.

    +-------+----------------------------+-----------------+
    | Style |       Example Output       |   Description   |
    +=======+============================+=================+
    | t     | 22:57                      | Short Time      |
    +-------+----------------------------+-----------------+
    | T     | 22:57:58                   | Long Time       |
    +-------+----------------------------+-----------------+
    | d     | 17/05/2016                 | Short Date      |
    +-------+----------------------------+-----------------+
    | D     | 17 May 2016                | Long Date       |
    +-------+----------------------------+-----------------+
    | f*    | 17 May 2016 22:57          | Short Date Time |
    +-------+----------------------------+-----------------+
    | F     | Tuesday, 17 May 2016 22:57 | Long Date Time  |
    +-------+----------------------------+-----------------+
    | R     | 5 years ago                | Relative Time   |
    +-------+----------------------------+-----------------+

    \* default

    Parameters
    ----------
    dt:
        The datetime to format.
        If this is a naive datetime, it is assumed to be local time.
    style:
        The style to format the datetime with. Defaults to ``f``.
    """
    if isinstance(dt, datetime.datetime):
        dt = dt.timestamp()
    return f"<t:{int(dt)}:{style}>"


class GuildNavigation(enum.StrEnum):
    customize = "customize"
    browse = "browse"
    guide = "guide"
    linked_roles = "linked-roles"

    @override
    def __str__(self) -> str:
        return f"<id:{self.value}>"

    @staticmethod
    def linked_role(role: disgrace.abc.Snowflake[RoleId], /) -> str:
        return f"<id:linked-roles:{role.id}>"
