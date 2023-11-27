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
from dataclasses import dataclass, field
from datetime import datetime, time

from mashumaro import field_options

from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.delivery_method.enums import DeliveryMethodStatus


@dataclass
class DeliveryMethod(SellerApiBaseModel):
    company_id: int
    """Идентификатор продавца."""
    created_at: datetime
    """Дата и время создания метода доставки."""
    updated_at: datetime
    """Дата и время последнего обновления метода метода доставки."""
    cutoff: time
    """Время до которого продавцу нужно собрать заказ."""
    name: str
    """Название метода доставки."""
    provider_id: int
    """Идентификатор службы доставки."""
    status: DeliveryMethodStatus
    """Статус метода доставки"""
    template_id: int
    """Идентификатор услуги по доставке заказа."""
    warehouse_id: int
    """Идентификатор склада."""
    id_: int = field(metadata=field_options(alias="id"))
    """Идентификатор метода доставки."""
