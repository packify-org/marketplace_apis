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
from urllib.parse import urljoin

from httpx import Auth

from marketplace_apis.common.requester import AsyncRequester, ApiRequestException
from marketplace_apis.yandex.campaign.methods import CampaignMethods
from marketplace_apis.yandex.oauth.methods import OAuthMethods

from marketplace_apis.yandex.offer_mapping.methods import OfferMappingMethods
from marketplace_apis.yandex.order.methods import OrderMethods

# from marketplace_apis.yandex.order.methods import OrderMethods
from marketplace_apis.yandex.warehouse.methods import WarehouseMethods


class MarketApiError(ApiRequestException):
    pass


class MarketApiAuth(Auth):
    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        yield request


class MarketApi(AsyncRequester):
    ENDPOINT = "https://api.partner.market.yandex.ru/"

    @staticmethod
    async def check_for_errors(func, self, *args, **kwargs):
        response_, data = await func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise MarketApiError(response_.json())
        return response_, data

    def build_campaign_url(self, endpoint):
        if not self.campaign_id:
            raise ValueError("campaign_id is None")  # noqa: TRY003
        return urljoin(f"campaigns/{self.campaign_id}/", endpoint)

    def build_business_url(self, endpoint):
        if not self.business_id:
            raise ValueError("business_id is None")  # noqa: TRY003
        return urljoin(f"businesses/{self.business_id}/", endpoint)

    oauth = OAuthMethods

    def __init__(
        self,
        token: str,
        campaign_id: str | None = None,
        business_id: str | None = None,
    ):
        super().__init__(
            self.ENDPOINT,
            headers={"Content-Type": "application/json"},
            auth=MarketApiAuth(token),
        )
        self.campaign_id = campaign_id
        self.business_id = business_id

        self.order = OrderMethods(self)
        self.offer_mapping = OfferMappingMethods(self)
        self.warehouse = WarehouseMethods(self)
        self.campaign = CampaignMethods(self)


if __name__ == "__main__":
    from pathlib import Path
    import os
    import time
    from datetime import timedelta

    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                os.environ[k] = v.strip()

    async def async_function():
        start_time_count = time.monotonic()
        async with MarketApi(
            os.getenv("TOKEN"), os.getenv("CAMPAIGN_ID"), os.getenv("BUSINESS_ID")
        ) as client:
            print(len(await client.offer_mapping.list_offer_mappings()))  # noqa: T201
        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time_count))  # noqa: T201

    asyncio.run(async_function())
    # print(api.warehouse.list_fby_warehouses())
    # print(api.warehouse.list_warehouses())
    # print(api.order.list_orders(status=OrderStatusType.PROCESSING)[-1])
    # print(MarketApi.oauth.get_tokens_by_code(
    #     os.getenv("CLIENT_ID"),
    #     os.getenv("CLIENT_SECRET"), 8863298
    # ))
    # print(
    #     MarketApi.oauth.get_tokens_by_refresh(
    #         os.getenv("CLIENT_ID"),
    #         os.getenv("CLIENT_SECRET"),
    #         os.getenv("REFRESH_TOKEN"),
    #     )
    # )
