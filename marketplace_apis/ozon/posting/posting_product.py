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


@dataclass
class ProductDimension(SellerApiBaseModel):
    height: str
    """Высота упаковки."""
    length: str
    """Длина товара."""
    weight: str
    """Вес товара в упаковке."""
    width: str
    """Ширина упаковки."""


@dataclass
class PostingProduct(SellerApiBaseModel):
    mandatory_mark: list[str]
    """Обязательная маркировка товара."""
    name: str
    """Название товара."""
    offer_id: str
    """Идентификатор товара в системе продавца — артикул."""
    price: str
    """Цена товара."""
    quantity: int
    """Количество товара в отправлении."""
    sku: int
    """Идентификатор товара в системе Ozon — SKU."""
    currency_code: Currency
    dimensions: ProductDimension | None = None
    """Размеры товара."""
    jw_uin: list[str] | None = None
    """Уникальный идентификационный номер (УИН) ювелирного изделия."""
