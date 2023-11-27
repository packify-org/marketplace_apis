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

from marketplace_apis.ozon.base import SellerApiBaseModel


@dataclass
class ProductStatusItemErrors(SellerApiBaseModel):
    code: str
    """Код ошибки."""
    state: str
    """Состояние товара, в котором произошла ошибка."""
    level: str
    """Уровень ошибки."""
    description: str
    """Описание ошибки."""
    field: str
    """Поле, в котором произошла ошибка."""
    attribute_id: int
    """Атрибут, в котором произошла ошибка."""
    attribute_name: str
    """Название атрибута, в котором произошла ошибка"""
    optional_description_elements: dict[str]
    """Дополнительные поля для описания ошибки."""


@dataclass
class ProductStatus(SellerApiBaseModel):
    state: str
    """Состояние товара."""
    state_failed: str
    """Состояние товара, на переходе в которое произошла ошибка."""
    moderate_status: str
    """Статус модерации."""
    decline_reasons: list[str]
    """Причины отклонения товара."""
    validation_state: str
    """Статус валидации."""
    state_name: str
    """Название состояния товара."""
    state_description: str
    """Описание состояния товара."""
    is_failed: bool
    """Признак, что при создании товара возникли ошибки."""
    is_created: bool
    """Признак, что товар создан."""
    state_tooltip: str
    """Подсказки для текущего состояния товара."""
    item_errors: list[ProductStatusItemErrors]
    """Ошибки при загрузке товаров."""
    state_updated_at: datetime
    """Время последнего изменения состояния товара."""
