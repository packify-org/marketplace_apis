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


@dataclass
class OrderDeliveryDates(MarketApiBaseModel):
    """Диапазон дат доставки."""

    fromDate: date
    """Ближайшая дата доставки."""
    toDate: date
    """Самая поздняя дата доставки.

    Если параметр ``toDate`` не указан, единственно возможной датой доставки считается
    дата, указанная в параметре ``fromDate``."""
    fromTime: time
    """Начало интервала времени доставки.

    Передается только совместно с параметром ``type=DELIVERY``.

    Формат времени: 24-часовой, ``ЧЧ:ММ``. В качестве минут всегда должно быть указано
    00 (исключение — 23:59)."""
    toTime: time
    """Конец интервала времени доставки.

    Передается только совместно с параметром ``type=DELIVERY``.

    Формат времени: 24-часовой, ``ЧЧ:ММ``. В качестве минут всегда должно быть указано
    00 (исключение — 23:59)."""
    realDeliveryDate: date | None = None
    """Дата, когда товар доставлен до пункта выдачи заказа (в случае самовывоза) или до
    покупателя (если заказ доставляет курьер)"""
