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


@dataclass
class OrderItemInstance(MarketApiBaseModel):
    cis: str
    """Код «Честного знака» без криптохвоста."""
    cisFull: str
    """Код «Честного знака» с криптохвостом."""
    uin: str
    """УИН ювелирного изделия (16-значный код) Производитель получает УИН
    когда регистрирует изделие в системе контроля за оборотом драгоценных металлов и
    камней — ГИИС ДМДК."""
    rnpt: str
    """Регистрационный номер партии товара.

    Представляет собой строку из четырех чисел, разделенных косой чертой:
    ХХХХХХХХ/ХХХХХХ/ХХХХХХХ/ХХХ.

    Первая часть — код таможни, которая зарегистрировала декларацию на партию товара.
    Далее — дата, номер декларации и номер маркированного товара в декларации."""
    gtd: str
    """Грузовая таможенная декларация.

    Представляет собой строку из трех чисел, разделенных косой чертой:
    ХХХХХХХХ/ХХХХХХ/ХХХХХХХ.

    Первая часть — код таможни, которая зарегистрировала декларацию на ввезенные товары.
    Далее — дата и номер декларации."""
