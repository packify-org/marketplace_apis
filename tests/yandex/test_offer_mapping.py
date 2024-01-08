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

from marketplace_apis.yandex.offer_mapping.offer_mapping import OfferMapping


@pytest.mark.asyncio
class TestOfferMapping:
    async def test_list_offer_mappings(self, market_api):
        async with market_api as client:
            offer_mappings = await client.offer_mapping.list_offer_mappings(iter_=False)
            assert isinstance(offer_mappings, list)
            assert isinstance(offer_mappings[0], OfferMapping)
