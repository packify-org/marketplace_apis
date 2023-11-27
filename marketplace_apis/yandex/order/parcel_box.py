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

from mashumaro import field_options

from marketplace_apis.yandex.base import MarketApiBaseModel


@dataclass
class OrderParcelBox(MarketApiBaseModel):
    """Информация о грузоместе."""

    fulfilmentId: str
    """Идентификатор грузового места в информационной системе магазина."""
    id_: int = field(metadata=field_options(alias="id"))
    """Идентификатор грузоместа."""
