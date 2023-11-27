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

from http import HTTPStatus

from httpx import Auth
from httpx_ratelimiter import LimiterTransport

from marketplace_apis.common.requester import Requester, ApiRequestException


class MarketApiError(ApiRequestException):
    pass


class MarketApiAuth(Auth):
    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        yield request


class MarketApiRequester(Requester):
    ENDPOINT = "https://api.partner.market.yandex.ru/campaigns/"

    @staticmethod
    def check_for_errors(func, self, *args, **kwargs):
        response_, data = func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise MarketApiError(response_.json())
        return response_, data

    def __init__(self, token: str, campaign_id: str):
        self.ENDPOINT = self.ENDPOINT + campaign_id + "/"
        limiter_transport = LimiterTransport(
            per_hour=1000000, max_delay=500, raise_when_fail=False
        )
        super().__init__(
            self.ENDPOINT,
            limiter_transport,
            headers={"Content-Type": "application/json"},
        )
        self.client.auth = MarketApiAuth(token)
