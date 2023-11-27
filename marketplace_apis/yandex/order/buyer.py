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

from mashumaro import field_options

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.enums import OrderBuyerType


@dataclass
class OrderBuyer(MarketApiBaseModel):
    """Информация о покупателе."""

    lastName: str
    """Фамилия покупателя."""
    firstName: str
    """Имя покупателя."""
    middleName: str
    """Отчество покупателя."""
    phone: str
    """Номер телефона покупателя.

    Формат номера: ``+<код_страны><код_региона><номер_телефона>``."""
    email: str
    """Адрес электронной почты покупателя.

    Допускается любой адрес электронной почты, соответствующий стандарту RFC 2822."""
    type_: OrderBuyerType = field(metadata=field_options(alias="type"))
    """Кто покупатель: физическое лицо или организация. Этот параметр используется
    FBS-магазинами, размещающими товары на витрине business.market.yandex.ru."""
    id_: str = field(metadata=field_options(alias="id"))
    """Идентификатор покупателя."""
