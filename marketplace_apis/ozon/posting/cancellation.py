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
from marketplace_apis.ozon.posting.enums import CancellationType


@dataclass
class Cancellation(SellerApiBaseModel):
    """Информация об отмене."""

    affect_cancellation_rating: bool
    """Если отмена влияет на рейтинг продавца — ``true``."""
    cancel_reason: str
    """Причина отмены."""
    cancel_reason_id: int
    """Идентификатор причины отмены отправления."""
    cancellation_initiator: str
    """Инициатор отмены отправления:

    * ``Клиент``,
    * ``Ozon``,
    * ``Продавец``.
    """
    cancellation_type: CancellationType
    """Тип отмены отправления:

        * ``client`` — клиентская.
        * ``ozon`` — отменено Ozon.
        * ``seller`` — отменено продавцом.
    """
    cancelled_after_ship: bool
    """Если отмена произошла после сборки отправления — ``true``."""
