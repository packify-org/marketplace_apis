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
from marketplace_apis.ozon.posting.posting import Posting
from tests.ozon.conftest import ValueStorage


@pytest.mark.asyncio
class TestPosting:
    async def test_list_postings(self, seller_api):
        async with seller_api as client:
            now = datetime.datetime.now()
            postings = await client.posting.list_postings(
                filter_since=now - datetime.timedelta(7),
                filter_to=now + datetime.timedelta(7),
                filter_status=PostingStatus.AWAITING_DELIVER,
            )
            ValueStorage.postings = postings
            assert isinstance(postings, list)
            assert isinstance(postings[0], Posting)

    async def test_get_by_number(self, seller_api):
        async with seller_api as client:
            posting = await client.posting.get_by_number(
                ValueStorage.postings[0].posting_number
            )
            assert isinstance(posting, Posting)

    async def test_label_task_create(self, seller_api):
        async with seller_api as client:
            task_id = await client.posting.label_task_create([
                ValueStorage.postings[0].posting_number
            ])
            assert isinstance(task_id, int)
