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


from marketplace_apis.common.enums import Currency
from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.buyer import OrderBuyer
from marketplace_apis.yandex.order.delivery import OrderDelivery
from marketplace_apis.yandex.order.enums import (
    OrderStatusType,
    OrderSubstatusType,
    OrderPaymentType,
    OrderPaymentMethodType,
    OrderTaxSystemType,
)
from marketplace_apis.yandex.order.item import OrderItem
from marketplace_apis.yandex.order.item_subsidy import OrderItemSubsidy


@dataclass
class Order(MarketApiBaseModel):
    status: OrderStatusType
    """Статус заказа"""
    substatus: OrderSubstatusType
    """Этап обработки заказа (если он имеет статус ``PROCESSING``) или причина отмены
    заказа (если он имеет статус ``CANCELLED``)."""
    creationDate: datetime
    """Дата и время оформления заказа."""
    currency: Currency
    """Валюта, в которой указаны цены товаров в заказе."""
    itemsTotal: float
    """Общая сумма заказа в валюте заказа без учета стоимости доставки и вознаграждения
    партнеру за скидки по промокодам, купонам и акциям (параметр ``subsidyTotal``).

    Для отделения целой части от дробной используется точка."""
    deliveryTotal: float
    """Стоимость доставки в валюте заказа."""
    buyerItemsTotal: float
    """Стоимость всех товаров в заказе в валюте покупателя после применения скидок и без
    учета стоимости доставки."""
    buyerTotal: float
    """Стоимость всех товаров в заказе в валюте покупателя после применения скидок и с
    учетом стоимости доставки."""
    buyerItemsTotalBeforeDiscount: float
    """Стоимость всех товаров в заказе в валюте покупателя до применения скидок и без
    учета стоимости доставки."""
    buyerTotalBeforeDiscount: float
    """Стоимость всех товаров в заказе в валюте покупателя до применения скидок и с
    учетом стоимости доставки."""
    paymentType: OrderPaymentType
    """Тип оплаты заказа."""
    paymentMethod: OrderPaymentMethodType
    """Способ оплаты заказа."""
    fake: bool
    """Тип заказа:

    * ``false`` — заказ покупателя.
    * ``true`` — тестовый заказ Маркета."""
    items: list[OrderItem]
    """Список товаров в заказе."""
    delivery: OrderDelivery
    """Информация о доставке."""
    taxSystem: OrderTaxSystemType
    """Система налогообложения (СНО) магазина на момент оформления заказа.
    Используется только совместно с параметром ``payment-method=YANDEX``."""
    cancelRequested: bool
    """Запрошена ли отмена."""
    id_: int
    """Идентификатор заказа."""
    subsidies: list[OrderItemSubsidy] | None = None
    """Список субсидий по типам."""
    buyer: OrderBuyer | None = None
    """Информация о покупателе."""
    notes: str | None = None
    """Комментарий к заказу."""
    expiryDate: datetime | None = None
    """Дата, после которой загруженный прайс-лист считается не актуальным и требует
    обновления."""
    total: float | None = None
    """Общая сумма заказа в валюте заказа с учетом стоимости доставки, но без учета
    вознаграждения партнеру за скидки по промокодам, купонам, кешбэку и акциям
    (параметр ``subsidyTotal``).

    Для отделения целой части от дробной используется точка."""
    subsidyTotal: float | None = None
    """Общее вознаграждение партнеру за скидки:

    * по промокодам;
    * по купонам;
    * по баллам кешбэка по подписке Яндекс Плюс;
    * по акциям.
    Передается в валюте, указанной в параметре ``currency``."""
    totalWithSubsidy: float | None = None
    """Сумма стоимости всех товаров в заказе и вознаграждения за них в валюте магазина
    (сумма параметров ``total`` и ``subsidyTotal``)"""
