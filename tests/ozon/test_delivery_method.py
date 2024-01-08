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

from marketplace_apis.ozon.delivery_method.delivery_method import DeliveryMethod


@pytest.mark.asyncio
class TestDeliveryMethod:
    async def test_list_delivery_methods(self, seller_api):
        async with seller_api as client:
            delivery_methods = await client.delivery_method.list_delivery_methods()
            assert isinstance(delivery_methods, list)
            assert isinstance(delivery_methods[0], DeliveryMethod)
