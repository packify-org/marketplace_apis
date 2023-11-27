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

from enum import StrEnum


class PrrOptionEnum(StrEnum):
    """Код услуги погрузочно-разгрузочных работ:

    * ``lift`` — подъём на лифте.
    * ``stairs`` — подъём по лестнице.
    * ``none`` — покупатель отказался от услуги, поднимать товары не нужно.
    * ``delivery_default`` — доставка включена в стоимость, по условиям оферты нужно
     доставить товар на этаж.
    Параметр актуален для КГТ-отправлений с доставкой силами продавца
     или интегрированной службой.
    """

    LIFT = "lift"
    """подъём на лифте"""
    STAIRS = "stairs"
    """подъём по лестнице"""
    NONE = "none"
    """покупатель отказался от услуги, поднимать товары не нужно"""
    DELIVERY_DEFAULT = "delivery_default"
    """доставка включена в стоимость,
     по условиям оферты нужно доставить товар на этаж"""
    NULL = ""
    """не указано"""


class TplIntegrationType(StrEnum):
    """Тип интеграции со службой доставки:

    * ``ozon`` — доставка службой Ozon.
    * ``3pl_tracking`` — доставка интегрированной службой.
    * ``non_integrated`` — доставка сторонней службой.
    * ``aggregator`` — доставка через партнёрскую доставку Ozon."""

    OZON = "ozon"
    """доставка службой Ozon"""
    THIRD_PL_TRACKING = "3pl_tracking"
    """доставка интегрированной службой"""
    NON_INTEGRATED = "non_integrated"
    """доставка сторонней службой"""
    AGGREGATOR = "aggregator"
    """доставка через партнёрскую доставку Ozon"""


class CancellationType(StrEnum):
    """Тип отмены отправления:

    * `client` — клиентская.
    * `ozon` — отменено Ozon.
    * `seller` — отменено продавцом.
    """

    CLIENT = "client"
    """клиентская отмена."""
    OZON = "ozon"
    """отменено Ozon."""
    SELLER = "seller"
    """отменено Продавцом."""
    NULL = ""
    """неизвестно"""


class PostingStatus(StrEnum):
    """Статус отправления:

    * ``acceptance_in_progress`` — идёт приёмка,
    * ``arbitration`` — арбитраж,
    * ``awaiting_approve`` — ожидает подтверждения,
    * ``awaiting_deliver`` — ожидает отгрузки,
    * ``awaiting_packaging`` — ожидает упаковки,
    * ``awaiting_registration`` — ожидает регистрации,
    * ``awaiting_verification`` — создано,
    * ``cancelled`` — отменено,
    * ``cancelled_from_split_pending`` — отменено,
    * ``client_arbitration`` — клиентский арбитраж доставки,
    * ``delivered`` — доставлено,
    * ``delivering`` — доставляется,
    * ``driver_pickup`` — у водителя,
    * ``not_accepted`` — не принят на сортировочном центре,
    * ``sent_by_seller`` — отправлено продавцом."""

    ACCEPTANCE_IN_PROGRESS = "acceptance_in_progress"
    """идёт приёмка"""
    ARBITRATION = "arbitration"
    """арбитраж"""
    AWAITING_APPROVE = "awaiting_approve"
    """ожидает подтверждения"""
    AWAITING_DELIVER = "awaiting_deliver"
    """ожидает отгрузки"""
    AWAITING_PACKAGING = "awaiting_packaging"
    """ожидает упаковки"""
    AWAITING_REGISTRATION = "awaiting_packaging"
    """ожидает регистрации"""
    AWAITING_VERIFICATION = "awaiting_verification"
    """создано"""
    CANCELLED = "cancelled"
    """отменено"""
    CANCELLED_FROM_SPLIT_PENDING = "cancelled_from_split_pending"
    """отменено"""
    CLIENT_ARBITRATION = "client_arbitration"
    """клиентский арбитраж доставки"""
    DELIVERED = "delivered"
    """доставлено"""
    DELIVERING = "delivering"
    """доставляется"""
    DRIVER_PICKUP = "driver_pickup"
    """у водителя"""
    NOT_ACCEPTED = "not_accepted"
    """не принят на сортировочном центре"""
    SENT_BY_SELLER = "sent_by_seller"
    """отправлено продавцом"""


class PostingSubstatus(StrEnum):
    """Подстатус отправления:

    * ``posting_acceptance_in_progress``— идёт приёмка,
    * ``posting_in_arbitration`` — арбитраж,
    * ``posting_created`` — создано,
    * ``posting_in_carriage`` — в перевозке,
    * ``posting_not_in_carriage`` — не добавлено в перевозку,
    * ``posting_registered`` — зарегистрировано,
    * ``posting_transferring_to_delivery`` `(status=awaiting_deliver)` — передаётся в доставку,
    * ``posting_awaiting_passport_data`` — ожидает паспортных данных,
    * ``posting_awaiting_registration`` — ожидает регистрации,
    * ``posting_registration_error`` — ошибка регистрации,
    * ``posting_transferring_to_delivery`` `(status=awaiting_registration)` — передаётся курьеру,
    * ``posting_split_pending`` — создано,
    * ``posting_canceled`` — отменено,
    * ``posting_in_client_arbitration`` — клиентский арбитраж доставки,
    * ``posting_delivered`` — доставлено,
    * ``posting_received`` — получено,
    * ``posting_conditionally_delivered`` — условно доставлено,
    * ``posting_in_courier_service`` — курьер в пути,
    * ``posting_in_pickup_point`` — в пункте выдачи,
    * ``posting_on_way_to_city`` — в пути в ваш город,
    * ``posting_on_way_to_pickup_point`` — в пути в пункт выдачи,
    * ``posting_returned_to_warehouse`` — возвращено на склад,
    * ``posting_transferred_to_courier_service`` — передаётся в службу доставки,
    * ``posting_driver_pick_up`` — у водителя,
    * ``posting_not_in_sort_center`` — не принято на сортировочном центре,
    * ``sent_by_seller`` — отправлено продавцом.
    """  # noqa: E501

    POSTING_ACCEPTANCE_IN_PROGRESS = "posting_acceptance_in_progress"
    """идёт приёмка"""
    POSTING_IN_ARBITRATION = "posting_in_arbitration"
    """арбитраж"""
    POSTING_IN_CARRIAGE = "posting_in_carriage"
    """в перевозке"""
    POSTING_NOT_IN_CARRIAGE = "posting_not_in_carriage"
    """не добавлено в перевозку"""
    POSTING_REGISTERED = "posting_registered"
    """зарегистрировано"""
    POSTING_TRANSFERRING_TO_DELIVERY = "posting_transferring_to_delivery"
    """передаётся в доставку или передается курьеру"""
    POSTING_AWAITING_PASSPORT_DATA = "posting_awaiting_passport_data"
    """ожидает паспортных данных"""
    POSTING_CREATED = "posting_created"
    """создано"""
    POSTING_AWAITING_REGISTRATION = "posting_awaiting_registration"
    """ожидает регистрации"""
    POSTING_REGISTRATION_ERROR = "posting_registration_error"
    """ошибка регистрации"""
    POSTING_SPLIT_PENDING = "posting_split_pending"
    """создано"""
    POSTING_CANCELED = "posting_canceled"
    """отменено"""
    POSTING_IN_CLIENT_ARBITRATION = "posting_in_client_arbitration"
    """клиентский арбитраж доставки"""
    POSTING_DELIVERED = "posting_delivered"
    """доставлено"""
    POSTING_RECEIVED = "posting_received"
    """получено"""
    POSTING_CONDITIONALLY_DELIVERED = "posting_conditionally_delivered"
    """условно доставлено"""
    POSTING_IN_COURIER_SERVICE = "posting_in_courier_service"
    """курьер в пути"""
    POSTING_IN_PICKUP_POINT = "posting_in_pickup_point"
    """в пункте выдачи"""
    POSTING_ON_WAY_TO_CITY = "posting_on_way_to_city"
    """в пути в ваш город"""
    POSTING_ON_WAY_TO_PICKUP_POINT = "posting_on_way_to_pickup_point"
    """в пути в пункт выдачи"""
    POSTING_RETURNED_TO_WAREHOUSE = "posting_returned_to_warehouse"
    """возвращено на склад"""
    POSTING_TRANSFERRED_TO_COURIER_SERVICE = "posting_transferred_to_courier_service"
    """передаётся в службу доставки"""
    POSTING_DRIVER_PICK_UP = "posting_driver_pick_up"
    """у водителя"""
    POSTING_NOT_IN_SORT_CENTER = "posting_not_in_sort_center"
    """не принято на сортировочном центре"""
    SENT_BY_SELLER = "sent_by_seller"
    """отправлено продавцом"""


class AsyncLabelGetStatus(StrEnum):
    """Статус формирования этикеток"""

    PENDING = "pending"
    """задание в очереди"""
    IN_PROGRESS = "in_progress"
    """формируются"""
    COMPLETED = "completed"
    """файл с этикетками готов"""
    ERROR = "error"
    """при формировании файла произошла ошибка"""
    FAILED = "failed"
    """при формировании файла произошла ошибка"""
