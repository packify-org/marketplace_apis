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
import datetime

import pytest

from marketplace_apis.ozon.posting.enums import PostingStatus
from marketplace_apis.ozon.product.product import Product
from tests.ozon.conftest import ValueStorage


@pytest.mark.asyncio
class TestProduct:
    async def test_list_info(self, seller_api):
        async with seller_api as client:
            now = datetime.datetime.now()
            posting = (
                await client.posting.list_postings(
                    filter_since=now - datetime.timedelta(7),
                    filter_to=now + datetime.timedelta(7),
                    filter_status=PostingStatus.AWAITING_DELIVER,
                    iter_=False,
                    limit=1,
                )
            )[0]
            product = await client.product.list_info(
                offer_id=[posting.products[0].offer_id]
            )
            ValueStorage.product = product[0]
            assert isinstance(product, list)
            assert isinstance(product[0], Product)

    async def test_list_attributes(self, seller_api):
        async with seller_api as client:
            attributes = await client.product.list_info(
                offer_id=[ValueStorage.product.offer_id]
            )
            assert isinstance(attributes, list)
            assert isinstance(attributes[0], Product)
