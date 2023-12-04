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

from marketplace_apis.common.utils import TranslatedStrEnum


class MarketplaceEnum(TranslatedStrEnum):
    __translations__ = {
        "ozon": "Ozon",
        "yandex_market": "Яндекс.Маркет",
        "wildberries": "Wildberries",
    }

    OZON = "ozon"
    YANDEX_MARKET = "yandex_market"
    WILDBERRIES = "wildberries"
