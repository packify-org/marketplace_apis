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
from datetime import date, time

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.enums import OrderParcelStatusType
from marketplace_apis.yandex.order.parcel_box import OrderParcelBox
from marketplace_apis.yandex.order.track import OrderTrack


@dataclass
class OrderShipment(MarketApiBaseModel):
    """Информация о посылках."""

    shipmentDate: date
    """День, в который нужно отгрузить заказ службе доставки."""
    id_: int
    """Идентификатор посылки, присвоенный Маркетом."""
    shipmentTime: time | None = None
    """Время, когда нужно отгрузить заказы службе доставки."""
    tracks: list[OrderTrack] | None = None
    """Информация для отслеживания перемещений посылки."""
    boxes: list[OrderParcelBox] | None = None
    """Список грузовых мест."""
    status: OrderParcelStatusType | None = None
    """Статус заказа в партнерской службе доставки."""
