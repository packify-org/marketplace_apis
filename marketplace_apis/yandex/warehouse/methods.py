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
from marketplace_apis.yandex.endpoints import API_PATH
from marketplace_apis.yandex.market_api_requester import MarketApiRequester
from marketplace_apis.yandex.warehouse.warehouses import Warehouses


class WarehouseMethods(ABCMethods):
    def __init__(self, requester: MarketApiRequester):
        super().__init__(requester)

    def list_fby_warehouses(self) -> Warehouses:
        """List all market FBY warehouses.
        :return: Warehouses object
        """
        _, data = self._requester.get(API_PATH["list_fby_warehouses"])
        return Warehouses.from_dict(data["result"])

    def list_warehouses(self) -> Warehouses:
        """List all warehouses.
        :return: Warehouses object
        """
        _, data = self._requester.get(
            self._requester.build_business_url(API_PATH["list_warehouses"])
        )
        return Warehouses.from_dict(data["result"])
