# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (C) 2023  Anatoly Raev
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime, UTC, tzinfo
from enum import StrEnum


def datetime_to_iso(dt: datetime, tz: tzinfo = UTC) -> str:
    """
    Converts a datetime object to an ISO formatted string, adjusting for a specified timezone.

    Parameters:
    dt (datetime): The datetime object to convert.
    tz (tzinfo, optional): The timezone to adjust the datetime object to. Defaults to UTC.

    Returns:
    str: The ISO formatted string representation of the datetime object.
    """
    if dt.tzinfo != tz:
        dt = dt.astimezone(tz)
    return dt.isoformat()


def dict_datetime_to_iso(dict_: dict, tz: tzinfo = UTC):
    """
    Recursively converts all datetime objects in a dictionary to their ISO representation.

    Parameters:
    dict_ (dict): The dictionary containing datetime objects to convert.
    tz (tzinfo, optional): The timezone to adjust the datetime objects to. Defaults to UTC.

    Returns:
    None
    """
    for k, v in dict_.items():
        if isinstance(v, datetime):
            dict_[k] = datetime_to_iso(v, tz)
        elif isinstance(v, dict):
            dict_datetime_to_iso(v, tz)


class TranslatedStrEnum(StrEnum):
    def translation(self) -> str:
        """
        Returns the Russian translation of the enumeration member.

        Returns:
        str: The Russian translation of the enumeration member.
        """
        if hasattr(self, "__translations__"):
            return self.__translations__[self.value]
        return self.name.capitalize()
