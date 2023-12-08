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


class OfferCardStatusType(StrEnum):
    """Статус карточки товара"""

    HAS_CARD_CAN_NOT_UPDATE = "HAS_CARD_CAN_NOT_UPDATE"
    """Карточка Маркета."""
    HAS_CARD_CAN_UPDATE = "HAS_CARD_CAN_UPDATE"
    """Можно дополнить."""
    HAS_CARD_CAN_UPDATE_ERRORS = "HAS_CARD_CAN_UPDATE_ERRORS"
    """Изменения не приняты."""
    HAS_CARD_CAN_UPDATE_PROCESSING = "HAS_CARD_CAN_UPDATE_PROCESSING"
    """Изменения на проверке."""
    NO_CARD_NEED_CONTENT = "NO_CARD_NEED_CONTENT"
    """Создайте карточку."""
    NO_CARD_MARKET_WILL_CREATE = "NO_CARD_MARKET_WILL_CREATE"
    """Создаст Маркет."""
    NO_CARD_ERRORS = "NO_CARD_ERRORS"
    """Не создана из-за ошибки."""
    NO_CARD_PROCESSING = "NO_CARD_PROCESSING"
    """Проверяем данные."""
    NO_CARD_ADD_TO_CAMPAIGN = "NO_CARD_ADD_TO_CAMPAIGN"
    """Разместите товар в магазине."""
