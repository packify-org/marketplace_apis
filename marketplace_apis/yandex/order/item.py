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
from marketplace_apis.yandex.order.enums import OrderVatType, OrderItemInstanceType
from marketplace_apis.yandex.order.item_detail import OrderItemDetail
from marketplace_apis.yandex.order.item_instance import OrderItemInstance
from marketplace_apis.yandex.order.item_promo import OrderItemPromo


@dataclass
class OrderItem(MarketApiBaseModel):
    """Товар в заказе."""

    feedId: int
    """Идентификатор каталога товаров."""
    offerId: str
    """Идентификатор вашего товарного предложения для определенного товара.
     `Описание поля в Справке для продавцов
     <https://yandex.ru/support/marketplace/assortment/fields/index.html#sku>`_"""
    feedCategoryId: str
    """Идентификатор категории, указанный в каталоге."""
    offerName: str
    """Название товара."""
    price: float
    """Цена товара в валюте заказа без учета вознаграждения партнеру за скидки по
    промокодам, купонам и акциям (параметр ``subsidy``).

    Для отделения целой части от дробной используется точка."""
    buyerPrice: float
    """Цена товара в валюте покупателя. В цене уже учтены скидки по:

    * акциям;
    * купонам;
    * промокодам.
    Для отделения целой части от дробной используется точка."""
    buyerPriceBeforeDiscount: float
    """Стоимость товара в валюте покупателя до применения скидок.

    Для отделения целой части от дробной используется точка."""
    priceBeforeDiscount: float
    """Стоимость товара в валюте магазина до применения скидок.

    Для отделения целой части от дробной используется точка."""
    count: int
    """Количество товара."""
    vat: OrderVatType
    """Ставка налога на добавленную стоимость (НДС) на товар."""
    shopSku: str
    """Ваш SKU."""
    subsidy: float
    """Общее вознаграждение партнеру за все скидки на товар:

    * по промокодам;
    * по купонам;
    * по баллам кешбэка по подписке Яндекс Плюс;
    * по акциям.
    Передается в валюте заказа, для отделения целой части от дробной используется
    точка."""
    partnerWarehouseId: str
    """Идентификатор склада в системе партнера, на который сформирован заказ.

    *Внимание!* Параметр устарел, временно поддерживается, но не доступен для ввода и
    редактирования."""
    id_: int = field(metadata=field_options(alias="id"))
    """Идентификатор товара в заказе."""
    promos: list[OrderItemPromo] | None = None
    """Информация о вознаграждениях партнеру за скидки на товар по промокодам, купонам
    и акциям."""
    instances: list[OrderItemInstance] | None = None
    """Информация о маркировке единиц товара.

    Возвращаются данные для маркировки, переданные в запросе
    ``PUT /campaigns/{campaignId}/orders/{orderId}/cis``.

    Если магазин еще не передавал коды для этого заказа, ``instances`` отсутствует."""

    details: list[OrderItemDetail] | None = None
    """Информация об удалении товара из заказа."""
    subsidies: list[OrderItemDetail] | None = None
    """Список субсидий по типам."""
    requiredInstanceTypes: list[OrderItemInstanceType] | None = None
    """Список необходимых маркировок товара."""
