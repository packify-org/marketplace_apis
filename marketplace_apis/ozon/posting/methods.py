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
from typing import Unpack

from marketplace_apis.common.base import ABCMethods
from marketplace_apis.common.requester import Requester
from marketplace_apis.common.utils import dict_datetime_to_iso
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.posting.label import AsyncLabelGetResult
from marketplace_apis.ozon.posting.methods_types import (
    ListPostings,
    GetPostingsWith,
    ShipPostingWith,
    ShipPostingProduct,
)
from marketplace_apis.ozon.posting.posting import Posting
from marketplace_apis.ozon.posting.ship import PostingShipResult
from marketplace_apis.ozon.utils import kwargs_to_filters


class PostingMethods(ABCMethods):
    def __init__(self, requester: Requester):
        super().__init__(requester)

    def list_postings(
        self,
        dir_: str = "desc",
        iter_: bool = True,
        limit: int = 1000,
        offset: int = 0,
        **kwargs: Unpack[ListPostings],
    ) -> list[Posting]:
        """List postings.
        :param limit: Maximum amount of Postings what will be retrieved in one request
        :param offset: Number of posting in this array from what response will be
        retrieved
        :param iter_: Whenever to get all postings by making multiple requests or not
        :param dir_: Direction of sorting - ``desc`` or ``asc``

        :return: List of postings
        """
        dict_datetime_to_iso(kwargs)
        raw_postings = []
        filter_, with_ = kwargs_to_filters(kwargs)

        def make_request():
            resp, decoded_resp = self._requester.post(
                API_PATH["list_postings"],
                data={
                    "limit": limit,
                    "offset": offset,
                    "dir": dir_,
                    "filter": filter_,
                    "with": with_,
                },
            )
            nonlocal raw_postings
            raw_postings += decoded_resp["result"]["postings"]
            return resp, decoded_resp

        _, data = make_request()
        while iter_ and data["result"]["has_next"]:
            offset += limit
            _, data = make_request()

        return [Posting.from_dict(raw_posting) for raw_posting in raw_postings]

    def get_by_number(self, posting_number: str, **kwargs: Unpack[GetPostingsWith]):
        _, with_ = kwargs_to_filters(kwargs)
        _, data = self._requester.post(
            API_PATH["get_posting_by_number"],
            data={"posting_number": posting_number, "with": with_},
        )
        return Posting.from_dict(data["result"])

    def label_task_create(self, posting_numbers: list[str]) -> int:
        _, data = self._requester.post(
            API_PATH["package_label_create"], data={"posting_number": posting_numbers}
        )
        return data["result"]["task_id"]

    def label_task_get(self, task_id: int) -> AsyncLabelGetResult:
        _, data = self._requester.post(
            API_PATH["package_label_get"], data={"task_id": task_id}
        )
        return AsyncLabelGetResult.from_dict(data["result"])

    def ship(
        self,
        posting_number,
        packages: list[list[ShipPostingProduct]],
        **kwargs: Unpack[ShipPostingWith],
    ) -> PostingShipResult:
        _, with_ = kwargs_to_filters(kwargs)
        _, data = self._requester.post(
            API_PATH["ship_posting"],
            data={
                "posting_number": posting_number,
                "with": with_,
                "packages": packages,
            },
        )
        return ShipPostingProduct.from_dict(data)
