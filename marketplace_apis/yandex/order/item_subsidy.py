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


from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.enums import OrderSubsidyType


@dataclass
class OrderItemSubsidy(MarketApiBaseModel):
    """Общее вознаграждение партнеру за все скидки на товар:

    * по промокодам;
    * по купонам;
    * по баллам кешбэка по подписке Яндекс Плюс;
    * по акциям.
    Передается в валюте заказа, для отделения целой части от дробной используется точка.
    """

    amount: float
    """Сумма субсидии."""
    type_: OrderSubsidyType
    """Тип субсидии."""
