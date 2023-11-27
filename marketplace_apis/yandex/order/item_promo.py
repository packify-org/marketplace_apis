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
from marketplace_apis.yandex.order.enums import OrderPromoType


@dataclass
class OrderItemPromo(MarketApiBaseModel):
    subsidy: float
    """Вознаграждение партнеру за скидку.

    Передается в валюте заказа, для отделения целой части от дробной используется
    точка."""
    type_: OrderPromoType = field(metadata=field_options(alias="type"))
    """Тип скидки"""
    discount: float | None = None
    """Размер пользовательской скидки в валюте покупателя."""
    shopPromoId: str | None = None
    """Идентификатор акции поставщика."""
    marketPromoId: str | None = None
    """Идентификатор акции в рамках соглашения на оказание услуг по продвижению сервиса
    между маркетплейсом Яндекс Маркета и партнером.

    Параметр передается, только если параметр ``type=MARKET_DEAL.``"""
