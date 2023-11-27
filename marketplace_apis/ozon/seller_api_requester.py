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


class SellerApiError(ApiRequestException):
    pass


class SellerApiAuth(Auth):
    def __init__(self, api_key: str, client_id: str):
        self.api_key = api_key
        self.client_id = client_id

    def auth_flow(self, request):
        request.headers["Client-Id"] = self.client_id
        request.headers["Api-Key"] = self.api_key
        yield request


class SellerApiRequester(Requester):
    ENDPOINT = "https://api-seller.ozon.ru/"

    @staticmethod
    def check_for_errors(func, self, *args, **kwargs):
        response_, data = func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise SellerApiError(response_.json())
        return response_, data

    def __init__(
        self,
        api_key: str,
        client_id: str,
        limiter_transport: LimiterTransport | None = None,
        use_limiter_transport: bool = True,
    ):
        if use_limiter_transport and limiter_transport is None:
            limiter_transport = LimiterTransport(
                per_second=10, max_delay=500, raise_when_fail=False
            )
        super().__init__(
            self.ENDPOINT,
            limiter_transport if use_limiter_transport else None,
            headers={"Content-Type": "application/json"},
        )
        self.client.auth = SellerApiAuth(api_key, client_id)
