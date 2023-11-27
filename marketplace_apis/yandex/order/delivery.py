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
from datetime import date

from mashumaro import field_options

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.courier import OrderCourier
from marketplace_apis.yandex.order.delivery_address import OrderDeliveryAddress
from marketplace_apis.yandex.order.delivery_dates import OrderDeliveryDates
from marketplace_apis.yandex.order.enums import (
    OrderDeliveryPartnerType,
    OrderDeliveryType,
    OrderVatType,
    OrderLiftType,
    OrderDeliveryDispatchType,
    OrderDeliveryEacType,
)
from marketplace_apis.yandex.order.region import Region
from marketplace_apis.yandex.order.shipment import OrderShipment
from marketplace_apis.yandex.order.track import OrderTrack


@dataclass
class OrderDelivery(MarketApiBaseModel):
    """Информация о доставке."""

    serviceName: str
    """Наименование службы доставки."""
    price: float
    """Стоимость доставки в валюте заказа.

    Для отделения целой части от дробной используется точка."""
    deliveryPartnerType: OrderDeliveryPartnerType
    """Тип сотрудничества со службой доставки в рамках конкретного заказа:

    Принимает значение ``YANDEX_MARKET`` — магазин работает со службой доставки через
    Маркет."""
    dates: OrderDeliveryDates
    """Диапазон дат доставки."""
    region: Region
    """Информация о регионах."""
    deliveryServiceId: int
    """Идентификатор службы доставки."""
    liftPrice: float
    """Стоимость подъема на этаж."""
    shipments: list[OrderShipment]
    """Информация о посылках."""
    type_: OrderDeliveryType = field(metadata=field_options(alias="type"))
    """Способ доставки заказа."""
    id_: int | None = field(default=None, metadata=field_options(alias="id"))
    """Идентификатор доставки, присвоенный магазином.

    Указывается, только если магазин передал данный идентификатор в ответе на запрос
    методом ``POST /cart.``"""
    address: OrderDeliveryAddress | None = None
    """Адрес доставки.

    Указывается, если ``type=DELIVERY`` или ``type=POST``."""
    vat: OrderVatType | None = None
    """Ставка налога на добавленную стоимость (НДС) на услугу доставки заказа
    Используется только совместно с параметром ``payment-method=YANDEX.``"""
    liftType: OrderLiftType | None = None
    """Тип подъема заказа на этаж."""
    outletStorageLimitDate: date | None = None
    """Дата, до которой заказ будет храниться в пункте выдачи. Возвращается, когда заказ
    переходит в статус PICKUP. Один раз дату можно поменять с помощью метода
    ``PUT campaigns/{campaignId}/orders/{orderId}/delivery/storage-limit``."""
    dispatchType: OrderDeliveryDispatchType | None = None
    """Способ отгрузки."""
    estimated: bool | None = None
    """Приблизительная ли дата доставки."""
    eacType: OrderDeliveryEacType | None = None
    """Тип кода подтверждения ЭАПП."""
    eacCode: str | None = None
    """Код подтверждения ЭАПП (для типа ``MERCHANT_TO_COURIER``)."""
    outletCode: str | None = None
    """Идентификатор пункта самовывоза, выбранного покупателем для получения заказа.

    Идентификатор указывается в личном кабинете магазина при создании или редактировании
    точки продаж.
    Параметр указывается, если ``type=PICKUP.``"""
    courier: OrderCourier | None = None
    """Информация о курьере."""
    tracks: list[OrderTrack] | None = None
    """Информация для отслеживания перемещений посылки."""
