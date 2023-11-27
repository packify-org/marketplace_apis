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


class OrderStatusType(StrEnum):
    """Статус заказа:

    * ``CANCELLED`` — заказ отменен.
    * ``DELIVERED`` — заказ получен покупателем.
    * ``DELIVERY`` — заказ передан в службу доставки.
    * ``PICKUP`` — заказ доставлен в пункт самовывоза.
    * ``PROCESSING`` — заказ находится в обработке.
    * ``UNPAID`` — заказ оформлен, но еще не оплачен (если выбрана оплата при оформлении).

    Также могут возвращаться другие значения. Обрабатывать их не требуется."""  # noqa: E501

    CANCELLED = "CANCELLED"
    """заказ отменен."""
    DELIVERED = "DELIVERED"
    """заказ получен покупателем."""
    DELIVERY = "DELIVERY"
    """заказ передан в службу доставки."""
    PICKUP = "PICKUP"
    """заказ доставлен в пункт самовывоза."""
    PROCESSING = "PROCESSING"
    """заказ находится в обработке."""
    UNPAID = "UNPAID"
    """заказ оформлен, но еще не оплачен (если выбрана оплата при оформлении)."""
    PLACING = "PLACING"
    RESERVED = "RESERVED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    PARTIALLY_RETURNED = "PARTIALLY_RETURNED"
    RETURNED = "RETURNED"
    CANCELLED_WITHOUT_REFUND = "CANCELLED_WITHOUT_REFUND"
    UNKNOWN = "UNKNOWN"


class OrderSubstatusType(StrEnum):
    """Этап обработки заказа (если он имеет статус ``PROCESSING``) или причина отмены
    заказа (если он имеет статус ``CANCELLED``).

    Возможные значения для заказа в статусе ``PROCESSING``:

    * ``STARTED`` — заказ подтвержден, его можно начать обрабатывать.
    * ``READY_TO_SHIP`` — заказ собран и готов к отправке.

    Возможные значения для заказа в статусе ``CANCELLED``:

    * ``PROCESSING_EXPIRED`` — значение более не используется.
    * ``REPLACING_ORDER`` — покупатель решил заменить товар другим по собственной инициативе.
    * ``RESERVATION_EXPIRED`` — покупатель не завершил оформление зарезервированного заказа в течение 10 минут.
    * ``SHOP_FAILED`` — магазин не может выполнить заказ.
    * ``USER_CHANGED_MIND`` — покупатель отменил заказ по личным причинам.
    * ``USER_NOT_PAID`` — покупатель не оплатил заказ (для типа оплаты ``PREPAID``) в течение 30 минут.
    * ``USER_REFUSED_DELIVERY`` — покупателя не устроили условия доставки.
    * ``USER_REFUSED_PRODUCT`` — покупателю не подошел товар.
    * ``USER_REFUSED_QUALITY`` — покупателя не устроило качество товара.
    * ``USER_UNREACHABLE`` — не удалось связаться с покупателем.

    Также могут возвращаться другие значения. Обрабатывать их не требуется."""  # noqa: E501

    STARTED = "STARTED"
    """заказ подтвержден, его можно начать обрабатывать."""
    READY_TO_SHIP = "READY_TO_SHIP"
    """заказ собран и готов к отправке."""
    PROCESSING_EXPIRED = "PROCESSING_EXPIRED"
    """значение более не используется."""
    REPLACING_ORDER = "REPLACING_ORDER"
    """покупатель решил заменить товар другим по собственной инициативе."""
    RESERVATION_EXPIRED = "RESERVATION_EXPIRED"
    """покупатель не завершил оформление зарезервированного заказа в течение
    10 минут."""
    SHOP_FAILED = "SHOP_FAILED"
    """магазин не может выполнить заказ."""
    USER_CHANGED_MIND = "USER_CHANGED_MIND"
    """покупатель отменил заказ по личным причинам."""
    USER_NOT_PAID = "USER_NOT_PAID"
    """покупатель не оплатил заказ (для типа оплаты PREPAID) в течение 30 минут."""
    USER_REFUSED_DELIVERY = "USER_REFUSED_DELIVERY"
    """покупателя не устроили условия доставки."""
    USER_REFUSED_PRODUCT = "USER_REFUSED_PRODUCT"
    """покупателю не подошел товар."""
    USER_REFUSED_QUALITY = "USER_REFUSED_QUALITY"
    """покупателя не устроило качество товара."""
    USER_UNREACHABLE = "USER_UNREACHABLE"
    """не удалось связаться с покупателем."""
    PENDING_EXPIRED = "PENDING_EXPIRED"
    SHOP_PENDING_CANCELLED = "SHOP_PENDING_CANCELLED"
    PENDING_CANCELLED = "PENDING_CANCELLED"
    USER_FRAUD = "USER_FRAUD"
    RESERVATION_FAILED = "RESERVATION_FAILED"
    USER_PLACED_OTHER_ORDER = "USER_PLACED_OTHER_ORDER"
    USER_BOUGHT_CHEAPER = "USER_BOUGHT_CHEAPER"
    MISSING_ITEM = "MISSING_ITEM"
    BROKEN_ITEM = "BROKEN_ITEM"
    WRONG_ITEM = "WRONG_ITEM"
    PICKUP_EXPIRED = "PICKUP_EXPIRED"
    DELIVERY_PROBLEMS = "DELIVERY_PROBLEMS"
    LATE_CONTACT = "LATE_CONTACT"
    CUSTOM = "CUSTOM"
    DELIVERY_SERVICE_FAILED = "DELIVERY_SERVICE_FAILED"
    WAREHOUSE_FAILED_TO_SHIP = "WAREHOUSE_FAILED_TO_SHIP"
    DELIVERY_SERIVCE_UNDELIVERED = "DELIVERY_SERIVCE_UNDELIVERED"
    DELIVERY_SERVICE_UNDELIVERED = "DELIVERY_SERVICE_UNDELIVERED"
    PREORDER = "PREORDER"
    AWAIT_CONFIRMATION = "AWAIT_CONFIRMATION"
    PACKAGING = "PACKAGING"
    SHIPPED = "SHIPPED"
    ASYNC_PROCESSING = "ASYNC_PROCESSING"
    USER_REFUSED_TO_PROVIDE_PERSONAL_DATA = "USER_REFUSED_TO_PROVIDE_PERSONAL_DATA"
    WAITING_USER_INPUT = "WAITING_USER_INPUT"
    WAITING_BANK_DECISION = "WAITING_BANK_DECISION"
    BANK_REJECT_CREDIT_OFFER = "BANK_REJECT_CREDIT_OFFER"
    CUSTOMER_REJECT_CREDIT_OFFER = "CUSTOMER_REJECT_CREDIT_OFFER"
    CREDIT_OFFER_FAILED = "CREDIT_OFFER_FAILED"
    AWAIT_DELIVERY_DATES_CONFIRMATION = "AWAIT_DELIVERY_DATES_CONFIRMATION"
    SERVICE_FAULT = "SERVICE_FAULT"
    DELIVERY_SERVICE_RECEIVED = "DELIVERY_SERVICE_RECEIVED"
    USER_RECEIVED = "USER_RECEIVED"
    WAITING_FOR_STOCKS = "WAITING_FOR_STOCKS"
    AS_PART_OF_MULTI_ORDER = "AS_PART_OF_MULTI_ORDER"
    READY_FOR_LAST_MILE = "READY_FOR_LAST_MILE"
    LAST_MILE_STARTED = "LAST_MILE_STARTED"
    ANTIFRAUD = "ANTIFRAUD"
    DELIVERY_USER_NOT_RECEIVED = "DELIVERY_USER_NOT_RECEIVED"
    DELIVERY_SERVICE_DELIVERED = "DELIVERY_SERVICE_DELIVERED"
    DELIVERED_USER_NOT_RECEIVED = "DELIVERED_USER_NOT_RECEIVED"
    USER_WANTED_ANOTHER_PAYMENT_METHOD = "USER_WANTED_ANOTHER_PAYMENT_METHOD"
    USER_RECEIVED_TECHNICAL_ERROR = "USER_RECEIVED_TECHNICAL_ERROR"
    USER_FORGOT_TO_USE_BONUS = "USER_FORGOT_TO_USE_BONUS"
    RECEIVED_ON_DISTRIBUTION_CENTER = "RECEIVED_ON_DISTRIBUTION_CENTER"
    DELIVERY_SERVICE_NOT_RECEIVED = "DELIVERY_SERVICE_NOT_RECEIVED"
    DELIVERY_SERVICE_LOST = "DELIVERY_SERVICE_LOST"
    SHIPPED_TO_WRONG_DELIVERY_SERVICE = "SHIPPED_TO_WRONG_DELIVERY_SERVICE"
    DELIVERED_USER_RECEIVED = "DELIVERED_USER_RECEIVED"
    WAITING_TINKOFF_DECISION = "WAITING_TINKOFF_DECISION"
    COURIER_SEARCH = "COURIER_SEARCH"
    COURIER_FOUND = "COURIER_FOUND"
    COURIER_IN_TRANSIT_TO_SENDER = "COURIER_IN_TRANSIT_TO_SENDER"
    COURIER_ARRIVED_TO_SENDER = "COURIER_ARRIVED_TO_SENDER"
    COURIER_RECEIVED = "COURIER_RECEIVED"
    COURIER_NOT_FOUND = "COURIER_NOT_FOUND"
    COURIER_NOT_DELIVER_ORDER = "COURIER_NOT_DELIVER_ORDER"
    COURIER_RETURNS_ORDER = "COURIER_RETURNS_ORDER"
    COURIER_RETURNED_ORDER = "COURIER_RETURNED_ORDER"
    WAITING_USER_DELIVERY_INPUT = "WAITING_USER_DELIVERY_INPUT"
    PICKUP_SERVICE_RECEIVED = "PICKUP_SERVICE_RECEIVED"
    PICKUP_USER_RECEIVED = "PICKUP_USER_RECEIVED"
    CANCELLED_COURIER_NOT_FOUND = "CANCELLED_COURIER_NOT_FOUND"
    COURIER_NOT_COME_FOR_ORDER = "COURIER_NOT_COME_FOR_ORDER"
    DELIVERY_NOT_MANAGED_REGION = "DELIVERY_NOT_MANAGED_REGION"
    INCOMPLETE_CONTACT_INFORMATION = "INCOMPLETE_CONTACT_INFORMATION"
    INCOMPLETE_MULTI_ORDER = "INCOMPLETE_MULTI_ORDER"
    INAPPROPRIATE_WEIGHT_SIZE = "INAPPROPRIATE_WEIGHT_SIZE"
    TECHNICAL_ERROR = "TECHNICAL_ERROR"
    SORTING_CENTER_LOST = "SORTING_CENTER_LOST"
    COURIER_SEARCH_NOT_STARTED = "COURIER_SEARCH_NOT_STARTED"
    LOST = "LOST"
    AWAIT_PAYMENT = "AWAIT_PAYMENT"
    AWAIT_LAVKA_RESERVATION = "AWAIT_LAVKA_RESERVATION"
    USER_WANTS_TO_CHANGE_ADDRESS = "USER_WANTS_TO_CHANGE_ADDRESS"
    FULL_NOT_RANSOM = "FULL_NOT_RANSOM"
    PRESCRIPTION_MISMATCH = "PRESCRIPTION_MISMATCH"
    DROPOFF_LOST = "DROPOFF_LOST"
    DROPOFF_CLOSED = "DROPOFF_CLOSED"
    DELIVERY_TO_STORE_STARTED = "DELIVERY_TO_STORE_STARTED"
    USER_WANTS_TO_CHANGE_DELIVERY_DATE = "USER_WANTS_TO_CHANGE_DELIVERY_DATE"
    WRONG_ITEM_DELIVERED = "WRONG_ITEM_DELIVERED"
    DAMAGED_BOX = "DAMAGED_BOX"
    AWAIT_DELIVERY_DATES = "AWAIT_DELIVERY_DATES"
    LAST_MILE_COURIER_SEARCH = "LAST_MILE_COURIER_SEARCH"
    PICKUP_POINT_CLOSED = "PICKUP_POINT_CLOSED"
    LEGAL_INFO_CHANGED = "LEGAL_INFO_CHANGED"
    USER_HAS_NO_TIME_TO_PICKUP_ORDER = "USER_HAS_NO_TIME_TO_PICKUP_ORDER"
    DELIVERY_CUSTOMS_ARRIVED = "DELIVERY_CUSTOMS_ARRIVED"
    DELIVERY_CUSTOMS_CLEARED = "DELIVERY_CUSTOMS_CLEARED"
    FIRST_MILE_DELIVERY_SERVICE_RECEIVED = "FIRST_MILE_DELIVERY_SERVICE_RECEIVED"
    AWAIT_AUTO_DELIVERY_DATES = "AWAIT_AUTO_DELIVERY_DATES"
    AWAIT_USER_PERSONAL_DATA = "AWAIT_USER_PERSONAL_DATA"
    NO_PERSONAL_DATA_EXPIRED = "NO_PERSONAL_DATA_EXPIRED"
    CUSTOMS_PROBLEMS = "CUSTOMS_PROBLEMS"
    AWAIT_CASHIER = "AWAIT_CASHIER"
    UNKNOWN = "UNKNOWN"


class OrderPaymentType(StrEnum):
    """Тип оплаты заказа:

    * ``PREPAID`` — оплата при оформлении заказа.
    * ``POSTPAID`` — оплата при получении заказа.

    Если параметр отсутствует, заказ будет оплачен при получении.
    """

    PREPAID = "PREPAID"
    """оплата при оформлении заказа"""
    POSTPAID = "POSTPAID"
    """оплата при получении заказа"""


class OrderPaymentMethodType(StrEnum):
    """Способ оплаты заказа.

    Возможные значения, если выбрана оплата при оформлении заказа ("paymentType": "PREPAID"):

    * ``YANDEX`` — банковской картой.
    * ``APPLE_PAY`` — Apple Pay.
    * ``GOOGLE_PAY`` — Google Pay.
    * ``CREDIT`` — в кредит.
    * ``TINKOFF_CREDIT`` — в кредит в Тинькофф Банке.
    * ``TINKOFF_INSTALLMENTS`` — рассрочка в Тинькофф Банке.
    * ``EXTERNAL_CERTIFICATE`` — подарочным сертификатом (например, из приложения «Сбербанк Онлайн»).
    * ``SBP`` — через систему быстрых платежей.

    Возможные значения, если выбрана оплата при получении заказа ("paymentType": "POSTPAID"):

    * ``CARD_ON_DELIVERY`` — банковской картой.
    * ``CASH_ON_DELIVERY`` — наличными.

    Значение по умолчанию: CASH_ON_DELIVERY.

    * ``B2B_ACCOUNT_PREPAYMENT`` — заказ оплачивает организация.
    * ``B2B_ACCOUNT_POSTPAYMENT`` - заказ оплачивает организация после доставки.
    """  # noqa: E501

    YANDEX = "YANDEX"
    """банковской картой"""
    APPLE_PAY = "APPLE_PAY"
    """Apple Pay"""
    GOOGLE_PAY = "GOOGLE_PAY"
    """Google Pay"""
    CREDIT = "CREDIT"
    """в кредит"""
    TINKOFF_CREDIT = "TINKOFF_CREDIT"
    """в кредит в Тинькофф Банке"""
    TINKOFF_INSTALLMENTS = "TINKOFF_INSTALLMENTS"
    """рассрочка в Тинькофф Банке"""
    EXTERNAL_CERTIFICATE = "EXTERNAL_CERTIFICATE"
    """подарочным сертификатом (например, из приложения «Сбербанк Онлайн»)"""
    SBP = "SBP"
    """через систему быстрых платежей"""
    CARD_ON_DELIVERY = "CARD_ON_DELIVERY"
    """банковской картой"""
    CASH_ON_DELIVERY = "CASH_ON_DELIVERY"
    """наличными"""
    B2B_ACCOUNT_PREPAYMENT = "B2B_ACCOUNT_PREPAYMENT"
    """заказ оплачивает организация"""
    B2B_ACCOUNT_POSTPAYMENT = "B2B_ACCOUNT_POSTPAYMENT"
    """заказ оплачивает организация после доставки"""


class OrderVatType(StrEnum):
    """Ставка налога на добавленную стоимость (НДС) на услугу доставки заказа:

    * ``NO_VAT`` — НДС не облагается, используется только для отдельных видов услуг.
    * ``VAT_0`` — НДС 0%. Например, используется при продаже товаров, вывезенных в таможенной процедуре экспорта, или при оказании услуг по международной перевозке товаров.
    * ``VAT_10_110`` — НДС 10/110. Расчетная ставка НДС 10%, применяется только для случая предоплаты.
    * ``VAT_20_120`` — НДС 20/120. Расчетная ставка НДС 20%, применяется только для случая предоплаты.
    * ``VAT_18_118`` — НДС 18/118. Ставка использовалась до 1 января 2019 года.

    Используется только совместно с параметром ``payment-method=YANDEX.``"""  # noqa: E501

    NO_VAT = "NO_VAT"
    """НДС не облагается, используется только для отдельных видов услуг."""
    VAT_0 = "VAT_0"
    """НДС 0%. Например, используется при продаже товаров, вывезенных в таможенной
    процедуре экспорта, или при оказании услуг по международной перевозке товаров."""
    VAT_10_110 = "VAT_10_110"
    """НДС 10/110. Расчетная ставка НДС 10%, применяется только для случая
    предоплаты."""
    VAT_20_120 = "VAT_20_120"
    """НДС 20/120. Расчетная ставка НДС 20%, применяется только для случая
    предоплаты."""
    VAT_18_118 = "VAT_18_118"
    """НДС 18/118. Ставка использовалась до 1 января 2019 года."""


class OrderPromoType(StrEnum):
    """Тип скидки"""

    MARKET_COUPON = "MARKET_COUPON"
    """скидка по промокоду от Маркета"""
    MARKET_DEAL = "MARKET_DEAL"
    """скидка в рамках соглашения на оказание услуг по продвижению сервиса между
    маркетплейсом Яндекс Маркета и партнером."""
    MARKET_COIN = "MARKET_COIN"
    """скидка по купонам."""
    DIRECT_DISCOUNT = "DIRECT_DISCOUNT"
    BLUE_SET = "BLUE_SET"
    BLUE_FLASH = "BLUE_FLASH"
    GENERIC_BUNDLE = "GENERIC_BUNDLE"
    MARKET_PROMOCODE = "MARKET_PROMOCODE"
    MARKET_BLUE = "MARKET_BLUE"
    MARKET_PRIME = "MARKET_PRIME"
    YANDEX_PLUS = "YANDEX_PLUS"
    BERU_PLUS = "BERU_PLUS"
    YANDEX_EMPLOYEE = "YANDEX_EMPLOYEE"
    LIMITED_FREE_DELIVERY_PROMO = "LIMITED_FREE_DELIVERY_PROMO"
    FREE_DELIVERY_THRESHOLD = "FREE_DELIVERY_THRESHOLD"
    MULTICART_DISCOUNT = "MULTICART_DISCOUNT"
    PRICE_DROP_AS_YOU_SHOP = "PRICE_DROP_AS_YOU_SHOP"
    FREE_DELIVERY_FOR_LDI = "FREE_DELIVERY_FOR_LDI"
    FREE_DELIVERY_FOR_LSC = "FREE_DELIVERY_FOR_LSC"
    SECRET_SALE = "SECRET_SALE"  # lol  # noqa: S105
    FREE_PICKUP = "FREE_PICKUP"
    CHEAPEST_AS_GIFT = "CHEAPEST_AS_GIFT"
    CASHBACK = "CASHBACK"
    SUPPLIER_MULTICART_DISCOUNT = "SUPPLIER_MULTICART_DISCOUNT"
    SPREAD_DISCOUNT_COUNT = "SPREAD_DISCOUNT_COUNT"
    SPREAD_DISCOUNT_RECEIPT = "SPREAD_DISCOUNT_RECEIPT"
    ANNOUNCEMENT_PROMO = "ANNOUNCEMENT_PROMO"
    DISCOUNT_BY_PAYMENT_TYPE = "DISCOUNT_BY_PAYMENT_TYPE"
    PERCENT_DISCOUNT = "PERCENT_DISCOUNT"
    EMPTY_PROMO = "EMPTY_PROMO"
    UNKNOWN = "UNKNOWN"


class OrderItemInstanceType(StrEnum):
    """Вид маркировки товара."""

    CIS = "CIS"
    UIN = "UIN"
    RNPT = "RNPT"
    GTD = "GTD"


class OrderItemStatusType(StrEnum):
    """Возвращенный или невыкупленный товар."""

    REJECTED = "REJECTED"
    """Невыкупленный товар"""
    RETURNED = "RETURNED"
    """Возвращенный товар"""


class OrderSubsidyType(StrEnum):
    """Тип субсидии."""

    NOT_SUBSIDY = "NOT_SUBSIDY"
    """Не субсидия"""
    SBER_SPASIBO = "SBER_SPASIBO"
    """СберСпасибо"""
    YANDEX_CASHBACK = "YANDEX_CASHBACK"
    """Яндекс.Кэшбек"""
    SUBSIDY = "SUBSIDY"
    """Субсидия"""
    DELIVERY = "DELIVERY"
    """Доставка"""


class OrderDeliveryType(StrEnum):
    """Способ доставки заказа"""

    DELIVERY = "DELIVERY"
    """курьерская доставка."""
    PICKUP = "PICKUP"
    """самовывоз."""
    POST = "POST"
    """почта."""


class OrderDeliveryPartnerType(StrEnum):
    """Тип сотрудничества со службой доставки в рамках конкретного заказа:

    Принимает значение ``YANDEX_MARKET`` — магазин работает со службой доставки через
    Маркет.
    """

    SHOP = "SHOP"
    """Доставка своими силами (rFBS)"""
    YANDEX_MARKET = "YANDEX_MARKET"
    """магазин работает со службой доставки через Маркет"""


class RegionType(StrEnum):
    """Тип региона."""

    CITY_DISTRICT = "CITY_DISTRICT"
    """район города"""
    CITY = "CITY"
    """крупный город"""
    CONTINENT = "CONTINENT"
    """континент"""
    COUNTRY_DISTRICT = "COUNTRY_DISTRICT"
    """область"""
    COUNTRY = "COUNTRY"
    """страна"""
    REGION = "REGION"
    """регион"""
    REPUBLIC_AREA = "REPUBLIC_AREA"
    """район субъекта федерации"""
    REPUBLIC = "REPUBLIC"
    """субъект федерации"""
    SUBWAY_STATION = "SUBWAY_STATION"
    """станция метро"""
    VILLAGE = "VILLAGE"
    """город"""
    OTHER = "OTHER"
    """неизвестный регион"""


class OrderLiftType(StrEnum):
    """Тип подъема заказа на этаж."""

    NOT_NEEDED = "NOT_NEEDED"
    """Не нужно"""
    MANUAL = "MANUAL"
    """Вручную по лестнице"""
    ELEVATOR = "ELEVATOR"
    """Пассажирский лифт"""
    CARGO_ELEVATOR = "CARGO_ELEVATOR"
    """Грузовой лифт"""
    FREE = "FREE"
    """Бесплатно"""
    UNKNOWN = "UNKNOWN"
    """Неизвестно"""


class OrderDeliveryDispatchType(StrEnum):
    """Способ отгрузки."""

    UNKNOWN = "UNKNOWN"
    """Неизвестно"""
    BUYER = "BUYER"
    """Покупателем"""
    MARKET_PARTNER_OUTLET = "MARKET_PARTNER_OUTLET"
    """Пункт выдачи партнера"""
    MARKET_BRANDED_OUTLET = "MARKET_BRANDED_OUTLET"
    """Брендированный пункт выдачи маркета"""
    SHOP_OUTLET = "SHOP_OUTLET"
    """Пункт выдачи магазина"""
    DROPOFF = "DROPOFF"
    """Dropoff"""


class OrderParcelStatusType(StrEnum):
    """Статус заказа в партнерской службе доставки."""

    NEW = "NEW"
    """Новый"""
    CREATED = "CREATED"
    """Создан"""
    READY_TO_SHIP = "READY_TO_SHIP"
    """Готов к отгрузке"""
    ERROR = "ERROR"
    """Ошибка"""
    UNKNOWN = "UNKNOWN"
    """Неизвестно"""


class OrderDeliveryEacType(StrEnum):
    """Тип кода подтверждения ЭАПП"""

    MERCHANT_TO_COURIER = "MERCHANT_TO_COURIER"
    """продавец передает код курьеру"""
    COURIER_TO_MERCHANT = "COURIER_TO_MERCHANT"
    """курьер передает код продавцу"""
    CHECKING_BY_MERCHANT = "CHECKING_BY_MERCHANT"
    """продавец проверяет код на своей стороне"""


class OrderBuyerType(StrEnum):
    """Кто покупатель"""

    PERSON = "PERSON"
    """физическое лицо"""
    BUSINESS = "BUSINESS"
    """организация"""


class OrderTaxSystemType(StrEnum):
    """Система налогообложения (СНО) магазина на момент оформления заказа"""

    ECHN = "ECHN"
    """единый сельскохозяйственный налог (ЕСХН)."""
    ENVD = "ENVD"
    """единый налог на вмененный доход (ЕНВД)."""
    OSN = "OSN"
    """общая система налогообложения (ОСН)."""
    PSN = "PSN"
    """патентная система налогообложения (ПСН)."""
    USN = "USN"
    """упрощенная система налогообложения (УСН)."""
    USN_MINUS_COST = "USN_MINUS_COST"
    """упрощенная система налогообложения, доходы, уменьшенные на величину расходов
    (УСН «Доходы минус расходы»)."""
