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
import contextlib
import functools
from http import HTTPStatus
from json import JSONDecodeError

import httpx
from httpx_ratelimiter import LimiterTransport


class ApiRequestException(Exception):
    pass


class Requester:
    """
    Class for making requests to some API. Usually this gets subclassed
    """

    @staticmethod
    def check_for_errors(func, self, *args, **kwargs):
        response_, data = func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise ApiRequestException(response_.status_code)
        return response_, data

    @staticmethod
    def _check_for_errors_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            return self.check_for_errors(func, self, *args, **kwargs)

        return wrapper

    def __init__(
        self,
        endpoint: str,
        limiter_transport: LimiterTransport | None,
        headers: dict[str] | None = None,
    ):
        if headers is None:
            headers = {}
        self.client = httpx.Client(
            transport=limiter_transport,
            headers=headers,
            base_url=endpoint,
        )
        self.client.headers["UserModel-Agent"] = "MarketplaceApis/0.1.0"

    @_check_for_errors_decorator
    def get(
        self, path: str, params: dict[str, str] | None = None, decode: bool = True
    ) -> tuple[httpx.Response, dict | bytes]:
        """
        Make get request to some path with url params
        :param path: url where make request to
        :param params: url params as dict what would be used to make request
        :param decode: whenever to decode response as json
        :return: Response object, dict with decoded content or None
        :rtype: tuple[Response, dict | bytes]
        """
        if params is None:
            params = {}
        response = self.client.get(path, params=params)
        decoded = response.content
        if decode:
            with contextlib.suppress(JSONDecodeError):
                decoded = response.json()
        return response, decoded

    @_check_for_errors_decorator
    def post(
        self,
        path: str,
        data: dict | None = None,
        params: dict[str, str] | None = None,
        decode: bool = True,
    ) -> tuple[httpx.Response, dict | bytes]:
        """
        Make post request to some path with url params
        :param path: url where make request to
        :param data: post body
        :param params: url params as dict what would be used to make request
        :param decode: whenever to decode response as json
        :return: Response object, dict with decoded content or None
        :rtype: tuple[Response, dict | bytes]
        """
        if data is None:
            data = {}
        if params is None:
            params = {}
        response = self.client.post(path, json=data, params=params)
        decoded = response.content
        if decode:
            with contextlib.suppress(JSONDecodeError):
                decoded = response.json()
        return response, decoded

    @_check_for_errors_decorator
    def put(
        self,
        path: str,
        data: dict | None = None,
        params: dict[str, str] | None = None,
        decode: bool = True,
    ) -> tuple[httpx.Response, dict | bytes]:
        """
        Make put request to some path with url params
        :param path: url where make request to
        :param data: put body
        :param params: url params as dict what would be used to make request
        :param decode: whenever to decode response as json
        :return: Response object, dict with decoded content or None
        :rtype: tuple[Response, dict | bytes]
        """
        if data is None:
            data = {}
        if params is None:
            params = {}
        response = self.client.put(path, json=data, params=params)
        decoded = response.content
        if decode:
            with contextlib.suppress(JSONDecodeError):
                decoded = response.json()
        return response, decoded


if __name__ == "__main__":
    from pathlib import Path

    requester = Requester(
        "https://cataas.com/",
    )
    resp, content = requester.get("cat", decode=False)
    with Path.open("test.png", "wb") as f:
        f.write(content)
