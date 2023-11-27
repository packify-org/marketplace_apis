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

from marketplace_apis.common.base import ABCMethods
from marketplace_apis.common.requester import Requester
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.product.product import Product


class ProductMethods(ABCMethods):
    def __init__(self, requester: Requester):
        super().__init__(requester)

    def list_info(
        self,
        offer_id: list[str] | None = None,
        product_id: list[int] | None = None,
        sku: list[int] | None = None,
    ) -> list[Product]:
        """List postings.
        :param offer_id: list of offer_id
        :param product_id: list of product_id
        :param sku: list of sku

        :return: List of Products
        """
        _, data = self.requester.post(
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
