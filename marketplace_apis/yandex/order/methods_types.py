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
from datetime import datetime, date
from enum import StrEnum
from typing import TypedDict, NotRequired

from marketplace_apis.yandex.order.enums import (
    OrderStatusType,
    OrderSubstatusType,
    OrderDeliveryDispatchType,
)


class ListOrders(TypedDict):
    status: NotRequired[OrderStatusType]
    """Статус заказа"""
    substatus: NotRequired[OrderSubstatusType]
    """Этап обработки заказа (если он имеет статус ``PROCESSING``) или причина отмены
    заказа (если он имеет статус ``CANCELLED``)."""
    fromDate: NotRequired[date | datetime]
    """Начальная дата для фильтрации заказов по дате оформления."""
    toDate: NotRequired[date | datetime]
    """Конечная дата для фильтрации заказов по дате оформления."""
    supplierShipmentDateFrom: NotRequired[date | datetime]
    """Начальная дата для фильтрации заказов по дате отгрузки в службу доставки
    (параметр ``shipmentDate``)."""
    supplierShipmentDateTo: NotRequired[date | datetime]
    """Конечная дата для фильтрации заказов по дате отгрузки в службу доставки (параметр
    ``shipmentDate``)."""
    updatedAtDateFrom: NotRequired[datetime]
    """Начальная дата для фильтрации заказов по дате и времени обновления (параметр
    ``updatedAt``)."""
    updatedAtDateTo: NotRequired[datetime]
    """Конечная дата для фильтрации заказов по дате и времени обновления (параметр
    updatedAt)."""
    dispatchType: NotRequired[OrderDeliveryDispatchType]
    """Способ отгрузки"""
    fake: NotRequired[bool]
    """Фильтрация заказов по типам:

    * ``false`` — заказ пользователя.
    * ``true`` — тестовый заказ Маркета."""
    hasCis: NotRequired[bool]
    """Нужно ли вернуть только те заказы, в составе которых есть хотя бы один товар с
    кодом идентификации из системы «Честный ЗНАК»:

    * ``true`` — да;
    * ``false`` — нет.

    Такие коды присваиваются товарам, которые подлежат маркировке и относятся к
    определенным категориям."""
    onlyWaitingForCancellationApprove: NotRequired[bool]
    """Фильтрация заказов по наличию запросов покупателей на отмену:

    ``true`` — возвращаются только заказы, которые находятся в статусе ``DELIVERY`` или
    ``PICKUP`` и которые пользователи решили отменить. Чтобы подтвердить или отклонить
    отмену, отправьте запрос
    ``PUT campaigns/{campaignId}/orders/{orderId}/cancellation/accept``."""
    onlyEstimatedDelivery: NotRequired[bool]
    """	Фильтрация заказов с долгой доставкой (31-60 дней) по подтвержденной дате
    доставки:

    * ``true`` — возвращаются только заказы с неподтвержденной датой доставки.
    * ``false`` — фильтрация не применяется."""


class PageFormatType(StrEnum):
    """Параметр управляет размещением ярлыков на странице"""

    A7 = "A7"
    """в PDF-файле будут странички размером A7, на каждой из которых разместится один
    ярлык"""
    A4 = "A4"
    """PDF-файл будет состоять из страниц A4, на каждой из которых будет по восемь
    ярлыков."""
