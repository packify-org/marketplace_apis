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
from datetime import datetime
from typing import TypedDict, NotRequired

from marketplace_apis.ozon.posting.enums import PostingStatus


class ListPostingsFilter(TypedDict):
    filter_delivery_method_id: NotRequired[int]
    """Идентификатор способа доставки."""
    filter_order_id: NotRequired[int]
    """Идентификатор заказа."""
    filter_provider_id: NotRequired[int]
    """Идентификатор службы доставки."""
    filter_since: datetime
    """Дата начала периода, за который нужно получить список отправлений.

    Формат `UTC`: ``ГГГГ-ММ-ДДTЧЧ:ММ:ССZ``.

    Пример: ``2019-08-24T14:15:22Z``."""
    filter_to: datetime
    """Дата конца периода, за который нужно получить список отправлений.

    Формат `UTC`: ``ГГГГ-ММ-ДДTЧЧ:ММ:ССZ``.

    Пример: ``2019-08-24T14:15:22Z``."""
    filter_status: NotRequired[PostingStatus]
    """Статус отправления"""
    filter_warehouse_id: NotRequired[None]
    """Идентификатор склада."""


class ListPostingsWith(TypedDict):
    with_analytics_data: NotRequired[bool]
    """Добавить в ответ данные аналитики."""
    with_barcodes: NotRequired[bool]
    """Добавить в ответ штрихкоды отправления."""
    with_financial_data: NotRequired[bool]
    """Добавить в ответ финансовые данные."""
    with_translit: NotRequired[bool]
    """Выполнить транслитерацию возвращаемых значений."""


class ShipPostingWith(TypedDict):
    with_additional_data: NotRequired[bool]
    """Добавить в ответ дополнительную информацию."""


class ListPostings(ListPostingsWith, ListPostingsFilter):
    pass


class GetPostingsWith(ListPostingsWith):
    product_exemplars: NotRequired[bool]
    """Добавить в ответ данные о продуктах и их экземплярах."""
    related_postings: NotRequired[bool]
    """Добавить в ответ номера связанных отправлений. Связанные отправления — те, на
    которое было разделено родительское отправление при сборке."""


class ShipPostingProduct(TypedDict):
    product_id: int
    """Идентификатор товара."""
    quantity: int
    """Количество экземпляров"""
