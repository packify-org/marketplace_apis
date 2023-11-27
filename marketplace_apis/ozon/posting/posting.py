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
from datetime import datetime

from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.posting.addressee import Addressee
from marketplace_apis.ozon.posting.analytics_data import AnalyticsData
from marketplace_apis.ozon.posting.barcodes import Barcodes
from marketplace_apis.ozon.posting.cancellation import Cancellation
from marketplace_apis.ozon.posting.courier import Courier
from marketplace_apis.ozon.posting.customer import Customer
from marketplace_apis.ozon.posting.delivery_method import DeliveryMethod
from marketplace_apis.ozon.posting.enums import (
    PrrOptionEnum,
    TplIntegrationType,
    PostingStatus,
    PostingSubstatus,
)
from marketplace_apis.ozon.posting.financial_data import FinancialData
from marketplace_apis.ozon.posting.posting_product import PostingProduct
from marketplace_apis.ozon.posting.product_exemplars import ProductExemplar
from marketplace_apis.ozon.posting.prr_option import PrrOption
from marketplace_apis.ozon.posting.requirements import Requirements


@dataclass
class Posting(SellerApiBaseModel):
    addressee: Addressee | None
    """Контактные данные получателя."""
    cancellation: Cancellation
    """Информация об отмене."""
    analytics_data: AnalyticsData | None
    """Данные аналитики."""
    barcodes: Barcodes | None
    """Штрихкоды отправления."""
    customer: Customer | None
    """Данные о покупателе."""
    delivering_date: datetime | None
    """Дата передачи отправления в доставку."""
    delivery_method: DeliveryMethod
    """Метод доставки."""
    financial_data: FinancialData | None
    """Данные о стоимости товара, размере скидки, выплате и комиссии."""
    in_process_at: datetime
    """Дата и время начала обработки отправления."""
    is_express: bool
    """Если использовалась быстрая доставка Ozon Express — ``true``."""
    is_multibox: bool
    """Признак, что в отправлении есть многокоробочный товар и нужно передать количество
    коробок для него:

    * ``true`` — до сборки передайте количество коробок через метод /v3/posting/multiboxqty/set.
    * ``false`` — отправление собрано с указанием количества коробок в параметре
    multi_box_qty или в отправлении нет многокоробочного товара."""  # noqa: E501
    multi_box_qty: int
    """Количество коробок, в которые упакован товар."""
    order_id: int
    """Идентификатор заказа, к которому относится отправление."""
    order_number: str
    """Номер заказа, к которому относится отправление."""
    parent_posting_number: str
    """Номер родительского отправления,
     в результате разделения которого появилось текущее."""
    posting_number: str
    """Номер отправления."""
    products: list[PostingProduct]
    """Список товаров в отправлении."""
    prr_option: PrrOption | PrrOptionEnum
    """Информация об услуге погрузочно-разгрузочных работ. Актуально для КГТ-отправлений
    с доставкой силами продавца или интегрированной службой."""
    requirements: Requirements
    """Список продуктов, для которых нужно передать страну-изготовителя, номер грузовой
     таможенной декларации (ГТД), регистрационный номер партии товара (РНПТ) или
     маркировку «Честный ЗНАК», чтобы перевести отправление в следующий статус."""
    shipment_date: datetime
    """Дата и время, до которой необходимо собрать отправление. Если отправление не
    собрать к этой дате — оно автоматически отменится."""
    status: PostingStatus
    substatus: PostingSubstatus
    tpl_integration_type: TplIntegrationType
    tracking_number: str
    related_postings: list[str] = field(
        metadata={"deserialize": lambda v: v["related_posting_numbers"]}, default=None
    )
    product_exemplars: list[ProductExemplar] = field(
        metadata={"deserialize": lambda v: v["products"]}, default=None
    )
    """Информация по продуктам и их экзмеплярам.

    Ответ содержит поле ``product_exemplars``, если в запросе передан признак
    ``with.product_exemplars = true``."""
    """Связанные отправления."""
    courier: Courier | None = None
    """Данные о курьере."""
    delivery_price: str | None = None
    """Стоимость доставки"""
    provider_status: str | None = None
    """Статус службы доставки."""
