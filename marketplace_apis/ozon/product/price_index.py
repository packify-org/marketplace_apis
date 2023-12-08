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

from marketplace_apis.common.enums import Currency
from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.product.enums import PriceIndex


@dataclass
class ProductPriceIndexData(SellerApiBaseModel):
    minimal_price: str
    """Минимальная цена товара"""
    minimal_price_currency: Currency
    """Валюта цены."""
    price_index_value: float
    """Значение индекса цены."""


@dataclass
class ProductPriceIndex(SellerApiBaseModel):
    external_index_data: ProductPriceIndexData
    """Цена товара у конкурентов на других площадках."""
    ozon_index_data: ProductPriceIndexData
    """Цена товара у конкурентов на Ozon."""
    self_marketplaces_index_data: ProductPriceIndexData
    """Цена вашего товара на других площадках."""
    price_index: PriceIndex
    """Итоговый ценовой индекс товара"""
