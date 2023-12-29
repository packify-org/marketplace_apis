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
from typing import TypedDict, NotRequired

from marketplace_apis.ozon.product.enums import Visibility


class ListAttributesFilter(TypedDict):
    offer_id: NotRequired[list[int]]
    """Фильтр по параметру offer_id. Можно передавать список значений."""
    product_id: NotRequired[list[int]]
    """Фильтр по параметру product_id. Можно передавать список значений."""
    visibility: NotRequired[Visibility]
    """Фильтр по видимости товара"""
