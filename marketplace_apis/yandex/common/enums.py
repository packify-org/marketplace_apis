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
from enum import StrEnum


class TimeUnitType(StrEnum):
    """Единица измерения времени:"""

    HOUR = "HOUR"
    """час"""
    DAY = "DAY"
    """сутки"""
    WEEK = "WEEK"
    """неделя"""
    MONTH = "MONTH"
    """месяц"""
    YEAR = "YEAR"
    """год"""


class AgeUnitType(StrEnum):
    """Единицы измерения возраста"""

    YEAR = "YEAR"
    MONTH = "MONTH"


class PlacementType(StrEnum):
    """Модель размещения"""

    FBS = "FBS"
    FBY = "FBY"
    DBS = "DBS"
    EXPRESS = "EXPRESS"
