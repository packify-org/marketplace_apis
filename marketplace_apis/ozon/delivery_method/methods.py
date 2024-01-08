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

from marketplace_apis.ozon.common.abc_methods import SellerApiABCMethods
from marketplace_apis.ozon.delivery_method.delivery_method import DeliveryMethod
from marketplace_apis.ozon.delivery_method.methods_types import (
    ListDeliveryMethodsFilter,
)
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.utils import kwargs_to_filters


class DeliveryMethodMethods(SellerApiABCMethods):
    async def list_delivery_methods(
        self,
        iter_: bool = True,
        limit: int = 1000,
        offset: int = 0,
        **kwargs: Unpack[ListDeliveryMethodsFilter],
    ) -> list[DeliveryMethod]:
        """List delivery methods.
        :param limit: Maximum amount of delivery methods what will be retrieved in one
        request
        :param offset: Number of delivery methods in this array from what response will
        be retrieved
        :param iter_: Whenever to get all postings by making multiple requests or not

        :return: List of delivery methods
        """
        raw_delivery_methods = []
        filter_, _ = kwargs_to_filters(kwargs)

        async def make_request():
            resp, decoded_resp = await self.client.post(
                API_PATH["list_delivery_methods"],
                data={
                    "limit": limit,
                    "offset": offset,
                    "filter": filter_,
                },
            )
            nonlocal raw_delivery_methods
            raw_delivery_methods += decoded_resp["result"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["has_next"]:
            offset += limit
            _, data = await make_request()

        return [
            DeliveryMethod.from_dict(raw_delivery_method)
            for raw_delivery_method in raw_delivery_methods
        ]
