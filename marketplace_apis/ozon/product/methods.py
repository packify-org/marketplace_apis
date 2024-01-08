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
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.product.methods_types import ListAttributesFilter
from marketplace_apis.ozon.product.product import Product


class ProductMethods(SellerApiABCMethods):
    async def list_info(
        self,
        offer_id: list[str] | None = None,
        product_id: list[int] | None = None,
        sku: list[int] | None = None,
    ) -> list[Product]:
        """List product infos.
        :param offer_id: list of offer_id
        :param product_id: list of product_id
        :param sku: list of sku

        :return: List of Products
        """
        _, data = await self.client.post(
            API_PATH["list_product_info"],
            data={
                "offer_id": offer_id,
                "product_id": product_id,
                "sku": sku,
            },
        )
        return [
            Product.from_dict(raw_product) for raw_product in data["result"]["items"]
        ]

    async def list_attributes(
        self,
        iter_: bool = True,
        limit: int = 1000,
        dir_="DESC",
        **kwargs: Unpack[ListAttributesFilter],
    ) -> list[Product]:
        """List product attributes.
        :param limit: Maximum amount of Product attributes what will be retrieved in one
        request
        :param iter_: Whenever to get all postings by making multiple requests or not
        :param dir_: Direction of sorting - ``DESC`` or ``ASC``

        :return: List of product attributes
        """

        raw_products = []

        async def make_request(last_id=None):
            resp, decoded_resp = await self.client.post(
                API_PATH["list_product_attributes"],
                data={
                    "limit": limit,
                    "sort_dir": dir_,
                    "filter": kwargs,
                }
                | ({"last_id": last_id} if last_id else {}),
            )
            nonlocal raw_products
            raw_products += decoded_resp["result"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["last_id"]:
            _, data = await make_request(data["last_id"])

        return [Product.from_dict(raw_product) for raw_product in raw_products]
