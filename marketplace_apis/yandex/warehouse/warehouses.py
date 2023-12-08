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
from marketplace_apis.yandex.warehouse.warehouse import Warehouse
from marketplace_apis.yandex.warehouse.warehouse_group import WarehouseGroup


@dataclass
class Warehouses(MarketApiBaseModel):
    """Информация о складах и группах складов."""

    warehouses: list[Warehouse]
    """Список складов, не входящих в группы. Информация о складе."""
    warehouseGroups: list[WarehouseGroup] | None = None
    """Список групп складов. Информация о группе складов."""
