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
from enum import StrEnum


class OfferConditionType(StrEnum):
    """Тип уценки."""

    PREOWNED = "PREOWNED"
    """бывший в употреблении товар, раньше принадлежал другому человеку."""
    SHOWCASESAMPLE = "SHOWCASESAMPLE"
    """витринный образец."""
    REFURBISHED = "REFURBISHED"
    """повторная продажа товара. Специальное значение для одежды, обуви и аксессуаров.
    Используется только для уцененных товаров из этой категории. Другие значения для
    одежды, обуви и аксессуаров не используются."""
    REDUCTION = "REDUCTION"
    """товар с дефектами."""
    RENOVATED = "RENOVATED"
    """восстановленный товар."""


class OfferConditionQualityType(StrEnum):
    """Внешний вид товара"""

    PERFECT = "PERFECT"
    EXCELLENT = "EXCELLENT"
    GOOD = "GOOD"


class OfferSellingProgramStatusType(StrEnum):
    """Информация о доступности или недоступности."""

    FINE = "FINE"
    REJECT = "REJECT"


@dataclass
class OfferType(StrEnum):
    """Особый тип товара.
    Указывается, если товар — книга, аудиокнига, лекарство, музыка, видео или
    поставляется под заказ."""

    DEFAULT = "DEFAULT"
    MEDICINE = "MEDICINE"
    BOOK = "BOOK"
    AUDIOBOOK = "AUDIOBOOK"
    ARTIST_TITLE = "ARTIST_TITLE"
    ON_DEMAND = "ON_DEMAND"


class OfferCampaignStatusType(StrEnum):
    """Статус товара"""

    PUBLISHED = "PUBLISHED"
    CHECKING = "CHECKING"
    DISABLED_BY_PARTNER = "DISABLED_BY_PARTNER"
    REJECTED_BY_MARKET = "REJECTED_BY_MARKET"
    DISABLED_AUTOMATICALLY = "DISABLED_AUTOMATICALLY"
    CREATING_CARD = "CREATING_CARD"
    NO_CARD = "NO_CARD"
    NO_STOCKS = "NO_STOCKS"
