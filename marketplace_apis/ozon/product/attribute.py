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

from marketplace_apis.ozon.base import SellerApiBaseModel


@dataclass
class AttributeValue(SellerApiBaseModel):
    dictionary_value_id: int
    """Идентификатор характеристики в словаре."""
    value: str
    """Значение характеристики товара."""


@dataclass
class Attribute(SellerApiBaseModel):
    attribute_id: int
    """Идентификатор характеристики."""
    complex_id: int
    """Идентификатор характеристики, которая поддерживает вложенные свойства. Например,
    у характеристики «Процессор» есть вложенные характеристики «Производитель» и
    «L2 Cache». У каждой из вложенных характеристик может быть несколько вариантов
    значений."""
    values: list[AttributeValue]
    """Массив значений характеристик."""


@dataclass
class ComplexAttribute(SellerApiBaseModel):
    attributes: list[Attribute]
    """Массив характеристик товара."""
