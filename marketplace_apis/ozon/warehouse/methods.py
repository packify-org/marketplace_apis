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
from typing import TYPE_CHECKING

from marketplace_apis.ozon.common.abc_methods import SellerApiABCMethods
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.warehouse.warehouse import Warehouse

if TYPE_CHECKING:
    pass


class WarehouseMethods(SellerApiABCMethods):
    async def list_warehouses(
        self,
    ) -> list[Warehouse]:
        """Получить все склады.

        # Возвращает: list[[Warehouse](warehouse.md)]
        """
        _, data = await self.client.post(API_PATH["list_warehouses"])
        return [Warehouse.from_dict(raw_warehouse) for raw_warehouse in data["result"]]
