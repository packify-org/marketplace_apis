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
class Requirements(SellerApiBaseModel):
    """Список продуктов, для которых нужно передать страну-изготовителя,
    номер грузовой таможенной декларации (ГТД), регистрационный номер партии товара (
    РНПТ) или маркировку «Честный ЗНАК», чтобы перевести отправление в следующий
    статус."""

    products_requiring_gtd: list[int]
    """Список идентификаторов товаров (SKU), для которых нужно передать номера
    таможенной декларации (ГТД).

    Для сборки отправления передайте для всех перечисленных товаров номер таможенной
    декларации или информацию о том, что номера нет, с помощью метода
    /v3/posting/fbs/ship/package или /v3/posting/fbs/ship."""
    products_requiring_country: list[int]
    """Список идентификаторов товаров (SKU), для которых нужно передать информацию о
    стране-изготовителе.

    Для сборки отправления передайте информацию о стране-изготовителе для всех
    перечисленных товаров с помощью метода /v2/posting/fbs/product/country/set"""
    products_requiring_mandatory_mark: list[int]
    """Список идентификаторов товаров (SKU),
     для которых нужно передать маркировку «Честный ЗНАК»."""
    products_requiring_jw_uin: list[int]
    """Список товаров, для которых нужно передать
     уникальный идентификационный номер (УИН) ювелирного изделия."""
    products_requiring_rnpt: list[int]
    """Список идентификаторов товаров (SKU), для которых нужно передать
     регистрационный номер партии товара (РНПТ)."""
