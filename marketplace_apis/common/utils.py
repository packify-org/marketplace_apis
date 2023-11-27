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


def datetime_to_iso(dt: datetime, tz: tzinfo = UTC) -> str:
    """Helper function to convert datetime to ISO string while converting it to some
    timezone"""
    # if dt is not in our timezone
    if dt.tzinfo != tz:
        dt = dt.astimezone(tz)
    return dt.isoformat()


def dict_datetime_to_iso(dict_: dict, tz: tzinfo = UTC):
    """Helper function to convert all datetime values to their ISO representation"""
    for k, v in dict_.items():
        if isinstance(v, datetime):
            dict_[k] = datetime_to_iso(v, tz)
        if isinstance(v, dict):
            dict_datetime_to_iso(v, tz)
