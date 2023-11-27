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

from marketplace_apis.ozon.delivery_method.enums import DeliveryMethodStatus


class ListDeliveryMethodsFilter(TypedDict):
    filter_provider_id: NotRequired[int]
    """Идентификатор службы доставки."""
    filter_status: NotRequired[DeliveryMethodStatus]
    """Статус метода доставки"""
    filter_warehouse_id: NotRequired[None]
    """Идентификатор склада."""
