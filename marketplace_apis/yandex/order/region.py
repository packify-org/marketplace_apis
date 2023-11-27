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
from typing import Self

from mashumaro import field_options

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.order.enums import RegionType


@dataclass
class Region(MarketApiBaseModel):
    """Информация о регионах."""

    name: str
    """Название региона."""
    type_: RegionType = field(metadata=field_options(alias="type"))
    """Тип региона."""
    id_: int = field(metadata=field_options(alias="id"))
    """Идентификатор региона."""
    parent: Self | None = None
    """Информация о родительском регионе.

    Указываются родительские регионы до уровня страны."""
    children: list[Self] | None = None
    """Дочерние регионы."""
