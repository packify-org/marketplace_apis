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
from enum import IntEnum, StrEnum
from typing import ClassVar

from marketplace_apis.common.utils import TranslatedStrEnum


class Day(IntEnum):
    """День недели"""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Currency(StrEnum):
    """Коды валют. Возможные значения:

    * `RUR` — российский рубль.
    * `RUB` — российский рубль.
    * `BYR` — белорусский рубль.
    * `BYN` — белорусский рубль.
    * `UAH` — украинская гривна.
    * `KZT` — казахстанский тенге.
    * `EUR` — евро.
    * `USD` — доллар США.
    * `CNY` — юань.
    """

    RUB = "RUB"
    """российский рубль"""
    RUR = "RUR"
    """российский рубль (Яндекс Маркет)"""
    BYN = "BYN"
    """белорусский рубль"""
    BYR = "BYN"
    """белорусский рубль (Яндекс Маркет)"""
    KZT = "KZT"
    """казахстанский тенге"""
    EUR = "EUR"
    """евро"""
    USD = "USD"
    """доллар США"""
    CNY = "CNY"
    """юань"""
    NONE = ""


class MarketplaceEnum(TranslatedStrEnum):
    __translations__: ClassVar = {
        "ozon": "Ozon",
        "yandex_market": "Яндекс.Маркет",
        "wildberries": "Wildberries",
    }

    OZON = "ozon"
    YANDEX_MARKET = "yandex_market"
    WILDBERRIES = "wildberries"
