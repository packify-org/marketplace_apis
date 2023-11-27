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
from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options

from marketplace_apis.common.currency import Currency
from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.product.attribute import Attribute, ComplexAttribute
from marketplace_apis.ozon.product.commision import ProductCommission
from marketplace_apis.ozon.product.enums import DimensionUnit
from marketplace_apis.ozon.product.file import ProductImage, ProductPDF
from marketplace_apis.ozon.product.price_index import ProductPriceIndex
from marketplace_apis.ozon.product.source import ProductSource
from marketplace_apis.ozon.product.status import ProductStatus
from marketplace_apis.ozon.product.stock import ProductStock
from marketplace_apis.ozon.product.visibility_details import ProductVisibilityDetails


@dataclass
class Product(SellerApiBaseModel):
    barcode: str
    """Штрихкод."""
    barcodes: list[str]
    """Все штрихкоды товара."""
    buybox_price: str
    """Цена главного предложения на Ozon.

    Устаревший параметр, больше не используется. Всегда возвращает пустую строку."""
    created_at: datetime
    """Дата и время создания товара."""
    fbo_sku: int
    """SKU товара, который продаётся со склада Ozon (FBO).

    С 15 августа 2023 года у товаров будет единый SKU и этот параметр будет отключён.
    Используйте значение этого параметра, если вы работаете по схеме FBO и в ответе нет
    параметра ``sku``."""
    fbs_sku: int
    """SKU товара, который продаётся со склада продавца (FBS и rFBS).

    С 15 августа 2023 года у товаров будет единый SKU и этот параметр будет отключён.
    Используйте значение этого параметра, если вы работаете по схеме FBO и в ответе нет
    параметра ``sku``."""
    has_discounted_item: bool
    """Признак, что у товара есть уценённые аналоги на складе Ozon."""
    is_discounted: bool
    """Признак, является ли товар уценённым:

    * Если товар создавался продавцом как уценённый — ``true``.
    * Если товар не уценённый или был уценён Ozon — ``false``."""
    discounted_stocks: ProductStock
    """Остатки уценённого товара на складе Ozon."""
    is_kgt: bool
    """Признак крупногабаритного товара."""
    currency_code: Currency
    """Валюта ваших цен. Совпадает с валютой, которая установлена в настройках личного
    кабинета."""
    marketing_price: str
    """Цена на товар с учетом всех акций. Это значение будет указано на витрине Ozon."""
    min_ozon_price: str
    """Минимальная цена на аналогичный товар на Ozon.

    Устаревший параметр, больше не используется. Всегда возвращает пустую строку."""
    min_price: str
    """Минимальная цена товара после применения акций."""
    old_price: str
    """Цена до учёта скидок. На карточке товара отображается зачёркнутой."""
    premium_price: str
    """Цена для клиентов с подпиской Ozon Premium."""
    price: str
    """Цена товара с учётом скидок — это значение показывается на карточке товара."""
    price_index: str
    """Параметр неактуален и будет удалён 1 мая 2023 года.

    Ценовой индекс."""
    price_indexes: ProductPriceIndex
    """Ценовые индексы товара."""
    recommended_price: str
    """Цена на товар, рекомендованная системой на основании схожих предложений."""
    status: ProductStatus
    """Описание состояния товара."""
    sources: list[ProductSource]
    """Информация об источниках схожих предложений."""
    stocks: ProductStock
    """Информация об остатках товара."""
    updated_at: datetime
    """Дата последнего обновления товара."""
    vat: str
    """Ставка НДС для товара."""
    visibility_details: ProductVisibilityDetails
    """Настройки видимости товара."""
    visible: bool
    """Если товар выставлен на продажу — ``true``."""
    description_category_id: int
    """Идентификатор категории. Используйте его с методами
    ``/v1/description-category/attribute`` и
    ``/v1/description-category/attribute/values.``"""
    color_image: str
    """Маркетинговый цвет."""
    images: list[ProductImage] | list[str]
    """Массив ссылок на изображения товара."""
    primary_image: str
    """Главное изображение товара."""
    images360: list[ProductImage] | list[str]
    """Массив изображений 360."""
    name: str
    """Название товара. До 500 символов."""
    offer_id: str
    """Идентификатор товара в системе продавца — артикул."""
    category_id: int
    """*Deprecated*. Alias to category_id.
    Идентификатор категории. Используйте его с методами ``/v2/category/tree``,
    ``/v3/category/attribute``, ``/v2/category/attribute/values``.

    Параметр будет отключён, когда отключат методы, указанные выше."""
    product_id: int | None = None
    """Идентификатор товара.  Same as ``id_``"""
    sku: int | None = None
    """SKU товара."""
    id_: int | None = field(default=None, metadata=field_options(alias="id"))
    """Идентификатор характеристики товара."""
    attributes: list[Attribute] | None = None
    """Массив характеристик товара."""
    commissions: list[ProductCommission] | None = None
    """Информация о комиссиях."""
    is_prepayment: bool | None = None
    """Флаг обязательной предоплаты для товара:

    * ``true`` — чтобы купить товар, нужно внести предоплату.
    * ``false`` — предоплата необязательна."""
    is_prepayment_allowed: bool | None = None
    """Если возможна предоплата — ``true``."""
    volume_weight: float | None = None
    """Объёмный вес товара."""
    complex_attributes: list[ComplexAttribute] | None = None
    """Массив вложенных характеристик."""
    height: int | None = None
    """Высота упаковки."""
    depth: int | None = None
    """Глубина."""
    width: int | None = None
    """Ширина упаковки."""
    dimension_unit: DimensionUnit | None = None
    """Единица измерения габаритов"""
    weight: int | None = None
    """Вес товара в упаковке."""
    weight_unit: str | None = None
    """Единица измерения веса."""
    image_group_id: str | None = None
    """Идентификатор для последующей пакетной загрузки изображений."""
    pdf_list: list[ProductPDF] | None = None
    """Массив PDF-файлов."""
    description: str | None = None
    """Описание."""
