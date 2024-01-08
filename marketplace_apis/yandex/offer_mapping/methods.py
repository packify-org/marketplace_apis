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

from marketplace_apis.yandex.common.abc_methods import MarketApiABCMethods
from marketplace_apis.yandex.endpoints import API_PATH
from marketplace_apis.yandex.offer_mapping.method_types import ListOfferMappings
from marketplace_apis.yandex.offer_mapping.offer_mapping import OfferMapping


class OfferMappingMethods(MarketApiABCMethods):
    async def list_offer_mappings(
        self, limit: int = 50, iter_: bool = True, **kwargs: Unpack[ListOfferMappings]
    ) -> list[OfferMapping]:
        """List offer mappings.
        :param limit: Maximum amount of offer mappings what will be retrieved in one
        request
        :param iter_: Whenever to get all offer mappings by making multiple requests or
        not

        :return: List of offer mappings
        """
        raw_offer_mappings = []

        page_token = None

        async def make_request():
            resp, decoded_resp = await self.client.post(
                self.client.build_business_url(API_PATH["list_offer_mappings"]),
                data=kwargs,
                params={
                    "limit": limit if not kwargs else None,
                    "page_token": page_token,
                },
            )
            nonlocal raw_offer_mappings
            raw_offer_mappings += decoded_resp["result"]["offerMappings"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and "nextPageToken" in data["result"]["paging"]:
            page_token = data["result"]["paging"]["nextPageToken"]
            _, data = await make_request()

        return [
            OfferMapping.from_dict(raw_offer_mapping)
            for raw_offer_mapping in raw_offer_mappings
        ]
