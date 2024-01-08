# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (C) 2024  Anatoly Raev
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
import pytest

from marketplace_apis.yandex.warehouse.warehouses import Warehouses


@pytest.mark.asyncio
class TestWarehouse:
    async def test_list_fby_warehouses(self, market_api):
        async with market_api as client:
            warehouses = await client.warehouse.list_fby_warehouses()
            assert isinstance(warehouses, Warehouses)

    async def test_list_warehouses(self, market_api):
        async with market_api as client:
            warehouses = await client.warehouse.list_warehouses()
            assert isinstance(warehouses, Warehouses)
