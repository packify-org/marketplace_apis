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

from dataclasses import dataclass
from datetime import date

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.enums import OrderItemStatusType


@dataclass
class OrderItemDetail(MarketApiBaseModel):
    updateDate: date | None = None
    """Формат даты: ДД-ММ-ГГГГ.
    Example: 23-09-2022"""
    itemCount: int | None = None
    """Количество единиц товара."""
    itemStatus: OrderItemStatusType | None = None
    """Возвращенный или невыкупленный товар."""
