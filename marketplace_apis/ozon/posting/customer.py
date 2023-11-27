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

from marketplace_apis.ozon.base import SellerApiBaseModel


@dataclass
class Address(SellerApiBaseModel):
    """Информация об адресе доставки."""

    comment: str
    """Комментарий к заказу."""
    address_tail: str
    """Адрес в текстовом формате."""
    zip_code: str
    """Почтовый индекс получателя."""
    country: str
    """Страна доставки."""
    region: str
    """Регион доставки."""
    city: str
    """Город доставки."""
    district: str
    """Район доставки."""
    latitude: float
    """Широта."""
    longitude: float
    """Долгота."""
    provider_pvz_code: str
    """Код пункта выдачи заказов 3PL провайдера."""
    pvz_code: int
    """Код пункта выдачи заказов."""


@dataclass
class Customer(SellerApiBaseModel):
    """Данные о покупателе."""

    address: Address
    """Информация об адресе доставки."""
    customer_email: str
    """Email покупателя."""
    customer_id: int
    """Идентификатор покупателя."""
    name: str
    """Имя покупателя."""
    phone: str
    """Контактный телефон. Всегда возвращает пустую строку."""
