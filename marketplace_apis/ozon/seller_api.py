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
from http import HTTPStatus

from httpx import Auth

from marketplace_apis.common.requester import AsyncRequester, ApiRequestException
from marketplace_apis.ozon.delivery_method.methods import DeliveryMethodMethods
from marketplace_apis.ozon.posting.methods import PostingMethods
from marketplace_apis.ozon.product.methods import ProductMethods
from marketplace_apis.ozon.warehouse.methods import WarehouseMethods


class SellerApiError(ApiRequestException):
    pass


class SellerApiAuth(Auth):
    def __init__(self, api_key: str, client_id: str):
        self.api_key = api_key
        self.client_id = client_id

    def auth_flow(self, request):
        request.headers["Client-Id"] = self.client_id
        request.headers["Api-Key"] = self.api_key
        yield request


class SellerApi(AsyncRequester):
    ENDPOINT = "https://api-seller.ozon.ru/"

    @staticmethod
    async def check_for_errors(func, self, *args, **kwargs):
        response_, data = await func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise SellerApiError(response_.json())
        return response_, data

    def __init__(
        self,
        api_key: str,
        client_id: str,
    ):
        super().__init__(
            self.ENDPOINT,
            headers={"Content-Type": "application/json"},
            auth=SellerApiAuth(api_key, client_id),
        )
        self.warehouse = WarehouseMethods(self)
        self.delivery_method = DeliveryMethodMethods(self)
        self.posting = PostingMethods(self)
        self.product = ProductMethods(self)


if __name__ == "__main__":
    from pathlib import Path
    import time
    import os
    from datetime import datetime, timedelta

    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                os.environ[k] = v.strip()

    async def async_function():
        start_time = datetime.now()
        start_time_count = time.monotonic()
        async with (os.getenv("API_KEY"), os.getenv("CLIENT_ID")) as client:
            print(  # noqa: T201
                await client.posting.list_postings(
                    filter_since=start_time - timedelta(14),
                    filter_to=start_time + timedelta(14),
                )
            )
        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time_count))  # noqa: T201

    asyncio.run(async_function())
    # print(api.posting.label_task_get(45342209))
    # [print([attribute.values[0].value for attribute in product.attributes if
    #         attribute.attribute_id == 4191]) for product in
    #  api.product.list_attribute()]
