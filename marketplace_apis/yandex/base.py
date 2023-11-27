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
from datetime import datetime, timedelta, tzinfo, UTC, date
from typing import ClassVar

from mashumaro.config import BaseConfig
from mashumaro.types import SerializationStrategy

from marketplace_apis.common.base import BaseModel


class UTC3Timezone(tzinfo):
    """A time zone with an arbitrary, constant +03:00 offset."""

    def utcoffset(self, _):  # noqa: PLR6301
        return timedelta(hours=3)

    def dst(self, _):  # noqa: PLR6301
        return timedelta()


class MarketApiUTC3Datetime(SerializationStrategy):
    FORMAT = "%d-%m-%Y %H:%M:%S"

    def serialize(self, value: datetime) -> str:
        value = value.astimezone(UTC3Timezone())
        return value.strftime(self.FORMAT)

    def deserialize(self, value: str) -> datetime:
        dt = datetime.strptime(value, self.FORMAT)
        dt.replace(tzinfo=UTC3Timezone())
        dt = dt.astimezone(UTC)
        return dt


class MarketApiDate(SerializationStrategy):
    FORMAT = "%d-%m-%Y"

    def serialize(self, value: date) -> str:
        return value.strftime(self.FORMAT)

    def deserialize(self, value: str) -> date:
        d = datetime.strptime(value, self.FORMAT).date()
        return d


class MarketApiBaseModel(BaseModel):
    class Config(BaseConfig):
        serialization_strategy: ClassVar = {
            datetime: MarketApiUTC3Datetime(),
            date: MarketApiDate(),
        }
