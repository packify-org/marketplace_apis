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
import os

from httpx_ratelimiter import LimiterTransport

from marketplace_apis.ozon.delivery_method.methods import DeliveryMethodMethods
from marketplace_apis.ozon.posting.methods import PostingMethods
from marketplace_apis.ozon.product.methods import ProductMethods
from marketplace_apis.ozon.seller_api_requester import SellerApiRequester
from marketplace_apis.ozon.warehouse.methods import WarehouseMethods


class SellerApi:
    def __init__(
        self,
        api_key: str,
        client_id: str,
        limiter_transport: LimiterTransport | None = None,
        use_limiter_transport: bool = True,
    ):
        self.requester = SellerApiRequester(
            api_key, client_id, limiter_transport, use_limiter_transport
        )
        self.posting = PostingMethods(self.requester)
        self.product = ProductMethods(self.requester)
        self.warehouse = WarehouseMethods(self.requester)
        self.delivery_method = DeliveryMethodMethods(self.requester)


if __name__ == "__main__":
    from pathlib import Path

    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                os.environ[k] = v.strip()

    api = SellerApi(os.getenv("API_KEY"), os.getenv("CLIENT_ID"))
    # print(api.posting.label_task_get(39116928))
    # [print([attribute.values[0].value for attribute in product.attributes if
    #         attribute.attribute_id == 4191]) for product in
    #  api.product.list_attribute()]
