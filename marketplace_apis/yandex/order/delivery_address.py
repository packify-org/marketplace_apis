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
from marketplace_apis.yandex.order.gps import Gps


@dataclass
class OrderDeliveryAddress(MarketApiBaseModel):
    """Адрес доставки."""

    country: str
    """Страна."""
    city: str
    """Город или населенный пункт."""
    house: str
    """Дом или владение."""
    gps: Gps
    """GPS-координаты."""
    district: str | None = None
    """Район."""
    postcode: str | None = None
    """Почтовый индекс.

    Указывается, если выбрана доставка почтой (``delivery type=POST``)."""
    subway: str | None = None
    """Станция метро."""
    block: str | None = None
    """Корпус или строение."""
    phone: str | None = None
    """Телефон получателя заказа."""
    recipient: str | None = None
    """Фамилия, имя и отчество получателя заказа."""
    entrance: str | None = None
    """Подъезд."""
    entryphone: str | None = None
    """Код домофона."""
    floor: str | None = None
    """Этаж."""
    apartment: str | None = None
    """Квартира или офис."""
    street: str | None = None
    """Улица."""
