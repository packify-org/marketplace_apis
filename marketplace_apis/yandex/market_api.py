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

from marketplace_apis.yandex.market_api_requester import MarketApiRequester
from marketplace_apis.yandex.oauth.methods import OAuthMethods
from marketplace_apis.yandex.order.methods import OrderMethods


class MarketApi:
    oauth = OAuthMethods

    def __init__(self, token: str, campaign_id: str):
        self.requester = MarketApiRequester(token, campaign_id)

        self.order = OrderMethods(self.requester)


if __name__ == "__main__":
    from pathlib import Path
    import os

    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                os.environ[k] = v.strip()

    api = MarketApi(os.getenv("TOKEN"), os.getenv("CAMPAIGN_ID"))
    print(api.order.list_orders()[-1])  # noqa: T201
    # MarketApi.oauth.get_tokens_by_code(
    #     os.getenv("CLIENT_ID"),
    #     os.getenv("CLIENT_SECRET"), 123456
    # )
