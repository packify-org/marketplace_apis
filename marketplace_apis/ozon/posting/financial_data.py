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

from marketplace_apis.common.currency import Currency
from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.posting.services import Services


@dataclass
class FinancialDataProduct(SellerApiBaseModel):
    """Товар в заказе для поля FinancialData."""

    actions: list[str]
    """Скидки."""
    currency_code: Currency
    client_price: str
    """Цена для клиента."""
    commission_amount: float
    """Размер комиссии за товар."""
    commission_percent: int
    """Процент комиссии."""
    item_services: Services
    """Услуги."""
    old_price: float
    """Цена до учёта скидок. На карточке товара отображается зачёркнутой."""
    payout: float
    """Выплата продавцу."""
    picking: None
    """Информация о доставке. Всегда возвращает ``null``."""
    price: float
    """Цена товара с учётом скидок — это значение показывается на карточке товара."""
    product_id: int
    """Идентификатор товара."""
    quantity: int
    """Количество товара в отправлении."""
    total_discount_percent: float
    """Процент скидки."""
    total_discount_value: float
    """Сумма скидки."""
    commissions_currency_code: Currency | None = None
    """Код валюты, в которой рассчитывались комиссии."""


@dataclass
class FinancialData(SellerApiBaseModel):
    """Данные о стоимости товара, размере скидки, выплате и комиссии."""

    cluster_from: str
    """Код региона, откуда отправляется заказ."""
    cluster_to: str
    """Код региона, куда доставляется заказ."""
    posting_services: Services
    """Услуги"""
    products: list[FinancialDataProduct]
    """Список товаров в заказе."""
