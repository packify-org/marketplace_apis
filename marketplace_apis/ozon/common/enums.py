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


class RegionType(StrEnum):
    """Тип региона."""

    CITY_DISTRICT = "CITY_DISTRICT"
    """район города"""
    CITY = "CITY"
    """крупный город"""
    CONTINENT = "CONTINENT"
    """континент"""
    COUNTRY_DISTRICT = "COUNTRY_DISTRICT"
    """область"""
    COUNTRY = "COUNTRY"
    """страна"""
    REGION = "REGION"
    """регион"""
    REPUBLIC_AREA = "REPUBLIC_AREA"
    """район субъекта федерации"""
    REPUBLIC = "REPUBLIC"
    """субъект федерации"""
    SUBWAY_STATION = "SUBWAY_STATION"
    """станция метро"""
    VILLAGE = "VILLAGE"
    """город"""
    OTHER = "OTHER"
    """неизвестный регион"""
