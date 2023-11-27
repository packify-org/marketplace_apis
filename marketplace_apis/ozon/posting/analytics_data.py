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
from datetime import datetime

from marketplace_apis.ozon.base import SellerApiBaseModel


@dataclass
class AnalyticsData(SellerApiBaseModel):
    """
    Данные аналитики.
    """

    city: str
    """Город доставки."""
    delivery_date_begin: datetime
    """Дата и время начала доставки."""
    delivery_date_end: datetime
    """Дата и время конца доставки."""
    delivery_type: str  # todo: get an Enum for this field
    """Способ доставки."""
    is_legal: bool
    """Признак, что получатель юридическое лицо:

    * ``true`` — юридическое лицо,
    * ``false`` — физическое лицо.
    """
    is_premium: bool
    """Наличие подписки Premium."""
    payment_type_group_name: str  # todo: get an Enum for this field
    """Способ оплаты."""
    region: str
    """Регион доставки."""
    tpl_provider: str
    """Служба доставки."""
    tpl_provider_id: int
    """Идентификатор службы доставки."""
    warehouse: str
    """Название склада отправки заказа."""
    warehouse_id: int
    """Идентификатор склада."""
