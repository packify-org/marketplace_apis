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
import asyncio
from typing import Unpack

from marketplace_apis.common.utils import dict_datetime_to_iso
from marketplace_apis.yandex.base import UTC3Timezone
from marketplace_apis.yandex.common.abc_methods import MarketApiABCMethods
from marketplace_apis.yandex.endpoints import API_PATH
from marketplace_apis.yandex.order.enums import OrderSubstatusType, OrderStatusType
from marketplace_apis.yandex.order.methods_types import ListOrders, PageFormatType
from marketplace_apis.yandex.order.order import Order


class OrderMethods(MarketApiABCMethods):
    async def list_orders(
        self,
        iter_: bool = True,
        page_size: int = 50,
        page: int = 1,
        **kwargs: Unpack[ListOrders],
    ) -> list[Order]:
        """List orders.
        :param page_size: Maximum amount of orders what will be retrieved in one request
        :param page: page from that order will be retrieved
        :param iter_: Whenever to get all postings by making multiple requests or not

        :return: List of orders
        """
        raw_orders = []
        if kwargs is None:
            kwargs = {}
        dict_datetime_to_iso(kwargs, tz=UTC3Timezone())
        url = self.client.build_campaign_url(API_PATH["list_orders"])

        async def make_request(page):
            resp, decoded_resp = await self.client.get(
                url, params={"pageSize": page_size, "page": page, **kwargs}
            )
            nonlocal raw_orders
            raw_orders += decoded_resp["orders"]
            return resp, decoded_resp

        _, data = await make_request(page)
        tasks = []
        while iter_ and data["pager"]["pagesCount"] != data["pager"]["currentPage"]:
            page += 1
            tasks.append(make_request(page))

        # Run all tasks concurrently
        await asyncio.gather(*tasks)

        return [Order.from_dict(raw_order) for raw_order in raw_orders]

    # TODO: implement this
    # def get_by_number(self, posting_number: str, with_: GetPostingsWith = None):
    #     if with_ is None:
    #         with_ = {}
    #     response, data = self._requester.post(
    #         API_PATH["get_posting_by_number"],
    #         data={"posting_number": posting_number, "with": with_},
    #     )
    #     return Posting.from_dict(data["result"])

    async def get_label(
        self, order_id: int, format_: PageFormatType | None = None
    ) -> bytes:
        """Get all labels for order in specified format.
        :param order_id: order id.
        :param format_: pdf file format. Defaults to A6

        :return: PDF-file with all labels"""
        _, data = await self.client.get(
            self._requester.build_campaign_url(
                f"orders/{order_id}/{API_PATH["get_delivery_labels"]}"
            ),
            params={"format": format_},
            decode=False,
        )
        return data

    async def update_status(
        self,
        order_id: int,
        status: OrderStatusType,
        substatus: OrderSubstatusType | None = None,
    ) -> Order:
        """Update status of order.
        :param order_id: order id.
        :param status: new status
        :param substatus: new substatus

        :return: updated order"""
        order_status_data = {"status": status}
        if substatus:
            order_status_data["substatus"] = substatus
        _, data = await self.client.put(
            self.client.build_campaign_url(
                f"orders/{order_id}/{API_PATH["order_status"]}"
            ),
            data={"order": order_status_data},
        )
        return Order.from_dict(data["order"])

    async def ship(self, order_id: int) -> Order:
        return await self.update_status(
            order_id,
            status=OrderStatusType.PROCESSING,
            substatus=OrderSubstatusType.READY_TO_SHIP,
        )
