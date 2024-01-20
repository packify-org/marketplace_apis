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
            raise MarketApiError(response_.status_code, response_.json())
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


class MarketApiFactory:
    def __init__(
        self, token: str, campaign_id: str | None = None, business_id: str | None = None
    ):
        self.token = token
        self.campaign_id = campaign_id
        self.business_id = business_id

    def __call__(self, *args, **kwargs) -> MarketApi:
        return MarketApi(self.token, self.campaign_id, self.business_id)


if __name__ == "__main__":
    from pathlib import Path
    import os
    from datetime import timedelta, datetime

    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                os.environ[k] = v.strip()

    async def main():
        # you don't have to pass campaign_id or business_id,
        # if you will not use methods, that require them
        market_api = MarketApiFactory(
            os.getenv("TOKEN"), os.getenv("CAMPAIGN_ID"), os.getenv("BUSINESS_ID")
        )
        async with market_api() as client:
            # print all orders from 14 days before now to now:
            now = datetime.now()
            orders = await client.order.list_orders(
                fromDate=(now - timedelta(14)).date(), toDate=now.date()
            )
            print(orders)
            # get offer_mappings of first order items
            order = orders[0]
            offer_ids = [item.offerId for item in order.items]
            offer_mappings = await client.offer_mapping.list_offer_mappings(
                offerIds=offer_ids
            )
            print(offer_mappings)

    asyncio.run(main())
