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
from marketplace_apis.yandex.common.enums import PlacementType
from marketplace_apis.yandex.offer.enums import OfferSellingProgramStatusType


@dataclass
class OfferSellingProgram(MarketApiBaseModel):
    """Информация о том, по каким моделям можно продавать товар, а по каким нельзя."""

    sellingProgram: PlacementType
    """Модель размещения."""
    status: OfferSellingProgramStatusType
    """Информация о том, можно ли по этой модели продавать товар."""
