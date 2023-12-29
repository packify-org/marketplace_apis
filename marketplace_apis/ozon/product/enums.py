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


class DimensionUnit(StrEnum):
    Millimeters = "mm"
    """миллиметры"""
    Centimeters = "cm"
    """сантиметры"""
    Inches = "in"
    """дюймы"""


class PriceIndex(StrEnum):
    """Итоговый ценовой индекс товара"""

    WITHOUT_INDEX = "WITHOUT_INDEX"
    PROFIT = "PROFIT"
    AVG_PROFIT = "AVG_PROFIT"
    NON_PROFIT = "NON_PROFIT"


class Visibility(StrEnum):
    """Фильтр по видимости товара"""

    ALL = "ALL"
    """все товары, кроме архивных."""
    VISIBLE = "VISIBLE"
    """товары, которые видны покупателям."""
    INVISIBLE = "INVISIBLE"
    """товары, которые не видны покупателям."""
    EMPTY_STOCK = "EMPTY_STOCK"
    """товары, у которых не указано наличие."""
    NOT_MODERATED = "NOT_MODERATED"
    """товары, которые не прошли модерацию."""
    MODERATED = "MODERATED"
    """товары, которые прошли модерацию."""
    DISABLED = "DISABLED"
    """товары, которые видны покупателям, но недоступны к покупке."""
    STATE_FAILED = "STATE_FAILED"
    """товары, создание которых завершилось ошибкой."""
    READY_TO_SUPPLY = "READY_TO_SUPPLY"
    """товары, готовые к поставке."""
    VALIDATION_STATE_PENDING = "VALIDATION_STATE_PENDING"
    """товары, которые проходят проверку валидатором на премодерации."""
    VALIDATION_STATE_FAIL = "VALIDATION_STATE_FAIL"
    """товары, которые не прошли проверку валидатором на премодерации."""
    VALIDATION_STATE_SUCCESS = "VALIDATION_STATE_SUCCESS"
    """товары, которые прошли проверку валидатором на премодерации."""
    TO_SUPPLY = "TO_SUPPLY"
    """товары, готовые к продаже."""
    IN_SALE = "IN_SALE"
    """товары в продаже."""
    REMOVED_FROM_SALE = "REMOVED_FROM_SALE"
    """товары, скрытые от покупателей."""
    BANNED = "BANNED"
    """заблокированные товары."""
    OVERPRICED = "OVERPRICED"
    """товары с завышенной ценой."""
    CRITICALLY_OVERPRICED = "CRITICALLY_OVERPRICED"
    """товары со слишком завышенной ценой."""
    EMPTY_BARCODE = "EMPTY_BARCODE"
    """товары без штрихкода."""
    BARCODE_EXISTS = "BARCODE_EXISTS"
    """товары со штрихкодом."""
    QUARANTINE = "QUARANTINE"
    """товары на карантине после изменения цены более чем на 50%."""
    ARCHIVED = "ARCHIVED"
    """товары в архиве."""
    OVERPRICED_WITH_STOCK = "OVERPRICED_WITH_STOCK"
    """товары в продаже со стоимостью выше, чем у конкурентов."""
    PARTIAL_APPROVED = "PARTIAL_APPROVED"
    """товары в продаже с пустым или неполным описанием."""
    IMAGE_ABSENT = "IMAGE_ABSENT"
    """товары без изображений."""
    MODERATION_BLOCK = "MODERATION_BLOCK"
    """товары, для которых заблокирована модерация."""
