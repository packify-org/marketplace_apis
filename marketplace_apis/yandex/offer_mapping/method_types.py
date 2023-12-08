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
from typing import TypedDict, NotRequired

from marketplace_apis.yandex.offer_card.enums import OfferCardStatusType


class ListOfferMappings(TypedDict):
    offerIds: NotRequired[list[str]]
    """	Идентификаторы товаров, информация о которых нужна.
    
    Такой список возвращается только целиком
    
    Если вы запрашиваете информацию по конкретным SKU, не заполняйте:
    
    * page_token;
    * limit;
    * cardStatuses;
    * categoryIds;
    * vendorNames;
    * tags;
    * archived.
    """
    cardStatuses: NotRequired[list[OfferCardStatusType]]
    """Фильтр по статусам карточек."""
    categoryIds: NotRequired[list[int]]
    """Фильтр по категориям на Маркете."""
    vendorNames: NotRequired[list[int]]
    """Фильтр по брендам."""
    tags: NotRequired[list[int]]
    """Фильтр по тегам."""
    archived: NotRequired[bool]
    """Фильтр по нахождению в архиве.

    Передайте true, чтобы получить товары, находящиеся в архиве. Если фильтр не заполнен
    или передано false, в ответе возвращаются товары, не находящиеся в архиве."""
