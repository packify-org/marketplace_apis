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


class DimensionUnit(StrEnum):
    Millimeters = "mm"
    """миллиметры"""
    Centimeters = "cm"
    """сантиметры"""
    Inches = "in"
    """дюймы"""


class PriceIndex(StrEnum):
    """Итоговый ценовой индекс товара"""

    WITHOUT_INDEX = "WITHOUT_INDEX"
    PROFIT = "PROFIT"
    AVG_PROFIT = "AVG_PROFIT"
    NON_PROFIT = "NON_PROFIT"
