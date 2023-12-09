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

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.common.age import Age
from marketplace_apis.yandex.common.time_period import TimePeriod
from marketplace_apis.yandex.offer.campaign_status import OfferCampaignStatus
from marketplace_apis.yandex.offer.condition import OfferCondition
from marketplace_apis.yandex.offer.enums import OfferType
from marketplace_apis.yandex.offer_card.enums import OfferCardStatusType
from marketplace_apis.yandex.offer.param import OfferParam
from marketplace_apis.yandex.offer.price import Price
from marketplace_apis.yandex.offer.price_with_discount import PriceWithDiscount
from marketplace_apis.yandex.offer.selling_program import OfferSellingProgram
from marketplace_apis.yandex.offer.weight_dimensions import OfferWeightDimensions


@dataclass
class Offer(MarketApiBaseModel):
    """Параметры товара."""

    offerId: str
    """Ваш SKU. Идентификатор товара в магазине.
    Разрешены английские и русские буквы, цифры и символы ``. , / \\ ( ) [ ] - = _``
    Максимальная длина — 80 знаков."""
    name: str
    """Составляйте название по схеме:
    тип + бренд или производитель + модель + особенности,
    если есть (например, цвет, размер или вес) и количество в упаковке.

    Не включайте в название условия продажи
    (например, «скидка», «бесплатная доставка» и т. д.),
    эмоциональные характеристики («хит», «супер» и т. д.).
    Не пишите слова большими буквами — кроме устоявшихся названий брендов и моделей.
    
    Оптимальная длина — 50–60 символов, максимальная — 150."""
    pictures: list[str]
    """Ссылки на изображения товара. Изображение по первой ссылке считается основным,
    остальные дополнительными.
    
    Требования к ссылкам:
    
    * Ссылок может быть до 10.
    * Указывайте ссылку целиком, включая протокол http или https.
    * Максимальная длина — 512 символов.
    * Русские буквы в URL можно.
    * Можно использовать прямые ссылки на изображения и на Яндекс Диск.
    * Ссылки на Яндекс Диске нужно копировать с помощью функции Поделиться. 
    * Относительные ссылки и ссылки на другие облачные хранилища — не работают
    
    * ✅ https://example-shop.ru/images/sku12345.jpg
    * ✅ https://yadi.sk/i/NaBoRsimVOLov
    * ❌ /images/sku12345.jpg 
    * ❌ https://www.dropbox.com/s/818f/tovar.jpg
    
    Ссылки на изображение должны быть постоянными. Нельзя использовать динамические
    ссылки, меняющиеся от выгрузки к выгрузке.
    
    Если нужно заменить изображение, выложите новое изображение по новой ссылке, а
    ссылку на старое удалите. Если просто заменить изображение по старой ссылке,
    оно не обновится."""
    barcodes: list[str]
    """Указывайте в виде последовательности цифр.
    Подойдут коды EAN-13, EAN-8, UPC-A, UPC-E или Code 128.
    
    Для книг указывайте ISBN.

    Для товаров определенных категорий и торговых марок штрихкод должен быть
    действительным кодом GTIN. Обратите внимание: внутренние штрихкоды,
    начинающиеся на 2 или 02, и коды формата Code 128 не являются GTIN."""
    cardStatus: OfferCardStatusType
    """Статус карточки товара."""
    sellingPrograms: list[OfferSellingProgram]
    """Информация о том, какие для товара доступны модели размещения. Информация о том,
    по каким моделям можно продавать товар, а по каким нельзя."""
    archived: bool
    """Товар помещен в архив."""
    videos: list[str] | None = None
    """Ссылка (URL) на видео товара.

    *Внимание! Пока действует временное ограничение: ссылка может быть только одна.*
    
    Требования к ссылке:
    
    * Указывайте ссылку целиком, включая протокол http или https.
    * Максимальная длина — 512 символов.
    * Русские буквы в URL можно.
    * Можно использовать прямые ссылки на видео и на Яндекс Диск.
    * Ссылки на Яндекс Диске нужно копировать с помощью функции Поделиться.
    * Относительные ссылки и ссылки на другие облачные хранилища — не работают
    
    * ✅ https://example-shop.ru/video/sku12345.avi
    * ✅ https://yadi.sk/i/NaBoRsimVOLov
    * ❌ /video/sku12345.avi
    * ❌ https://www.dropbox.com/s/818f/super-tovar.avi
    
    Ссылки на видео должны быть постоянными. Нельзя использовать динамические ссылки,
    меняющиеся от выгрузки к выгрузке.
    
    Если нужно заменить видео, выложите новое видео по новой ссылке, а ссылку на старое
    удалите. Если просто заменить видео по старой ссылке, оно не обновится.
    """
    vendorCode: str | None = None
    """Артикул товара от производителя."""
    tags: list[str] | None = None
    """Метки товара, используемые магазином. Покупателям теги не видны.
    По тегам можно группировать и фильтровать разные товары в каталоге — например,
    товары одной серии, коллекции или линейки.

    Максимальная длина тега 20 символов. У одного товара может быть максимум 10 тегов.
    Всего можно создать не больше 50 разных тегов."""
    shelfLife: TimePeriod | None = None
    """Срок годности — период, по прошествии которого товар становится непригоден.

    Указывайте срок, указанный на банке или упаковке. Текущая дата, дата поставки или
    дата отгрузки значения не имеет.

    Обязательно указывайте срок, если он есть.

    В комментарии укажите условия хранения. Например, «Хранить в сухом помещении»."""
    lifeTime: TimePeriod | None = None
    """Срок службы — период, в течение которого товар должен исправно выполнять свою
    функцию.

    Обязательно указывайте срок, если он есть.

    В комментарии укажите условия хранения. Например, «Использовать при температуре не
    ниже −10 градусов»."""
    guaranteePeriod: TimePeriod | None = None
    """Гарантийный срок — период, в течение которого можно бесплатно заменить или
    починить товар.

    Обязательно указывайте срок, если он есть.

    В комментарии опишите особенности гарантийного обслуживания. Например,
    «Гарантия на аккумулятор — 6 месяцев»."""
    customsCommodityCode: str | None = None
    """Код товара в единой Товарной номенклатуре внешнеэкономической деятельности
    (ТН ВЭД) — 10 или 14 цифр без пробелов.

    Обязательно укажите, если он есть."""
    certificates: list[str] | None = None
    """Номера документов на товар: сертификата, декларации соответствия и т. п.

    Передавать можно только номера документов, сканы которого загружены в личном
    кабинете продавца по инструкции."""
    boxCount: int | None = None
    """Количество грузовых мест.

    Параметр используется, если товар представляет собой несколько коробок, упаковок и
    так далее. Например, кондиционер занимает два места — внешний и внутренний блоки в
    двух коробках.

    Для товаров, занимающих одно место, не передавайте этот параметр."""
    condition: OfferCondition | None = None
    """Состояние уцененного товара.

    Используется только для товаров, продаваемых с уценкой."""
    type_: OfferType | str | None = None
    """Особый тип товара. Указывается, если товар — книга, аудиокнига, лекарство,
    музыка, видео или поставляется под заказ."""
    downloadable: bool | None = None
    """Признак цифрового товара. Укажите true, если товар доставляется по электронной
    почте."""
    adult: bool | None = None
    """Параметр включает для товара пометку 18+. Устанавливайте ее только для товаров,
    которые относятся к удовлетворению сексуальных потребностей."""
    age: Age | None = None
    """Если товар не предназначен для детей младше определенного возраста, укажите это.

    Возрастное ограничение можно задавать в годах (с нуля, с 6, 12, 16 или 18) или в
    месяцах (любое число от 0 до 12)."""
    params: list[OfferParam] | None = None
    """Характеристики, которые есть только у товаров конкретной категории — например,
    диаметр колес велосипеда или материал подошвы обуви."""

    purchasePrice: Price | None = None
    """Себестоимость — затраты на самостоятельное производство товара или закупку у
    производителя или поставщиков. Цена на товар. Время последнего обновления."""
    additionalExpenses: Price | None = None
    """Дополнительные расходы на товар. Например, на доставку или упаковку. Цена на
    товар. Время последнего обновления."""
    cofinancePrice: Price | None = None
    """Цена для скидок с Маркетом. Маркет может компенсировать до половины скидки.
    Назначьте минимальную цену до вычета тарифов, по которой готовы продавать товар,
    а мы рассчитаем скидку и размер софинансирования. Если Маркет не готов
    софинансировать скидку, покупатель её не увидит. Цена на товар. Время последнего
    обновления."""
    description: str | None = None
    """	Подробное описание товара: например, его преимущества и особенности.

    Не давайте в описании инструкций по установке и сборке.
    Не используйте слова «скидка», «распродажа», «дешевый», «подарок»
    (кроме подарочных категорий), «бесплатно», «акция», «специальная цена», «новинка»,
    «new», «аналог», «заказ», «хит».
    Не указывайте никакой контактной информации и не давайте ссылок.

    Можно использовать теги:

    * ``<h>``, ``<h1>``, ``<h2>`` и так далее — для заголовков;
    * ``<br>`` и ``<p>`` — для переноса строки;
    * ``<ol>`` — для нумерованного списка;
    * ``<ul>`` — для маркированного списка;
    * ``<li>`` — для создания элементов списка (должен находиться внутри <ol> или <ul>);
    * ``<div>`` — поддерживается, но не влияет на отображение текста.

    Оптимальная длина — 400–600 символов, максимальная — 6000."""
    vendor: str | None = None
    """Название бренда или производителя. Должно быть записано так, как его пишет сам
    бренд."""
    manufacturerCountries: list[str] | None = None
    """Страна, где был произведен товар. Записывайте названия стран так, как они
    записаны в списке."""
    weightDimensions: OfferWeightDimensions | None = None
    """Габариты упаковки и вес товара."""
    campaigns: list[OfferCampaignStatus] | None = None
    """Список магазинов, в которых размещен товар. Статус товара в магазине."""
    category: str | None = None
    """Категория, к которой магазин относит свой товар. Она помогает точнее определить
    для товара категорию в каталоге Маркета.

    Указывайте конкретные категории — например, набор ножей лучше отнести к категории
    Столовые приборы, а не просто Посуда.

    Выбирайте категории, которые описывают товар, а не абстрактный признак — например,
    Духи, а не Подарки."""
    basicPrice: PriceWithDiscount | None = None
    """Цена. Цена с указанием скидки. Время последнего обновления."""