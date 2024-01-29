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
import asyncio
import contextlib
import functools
from http import HTTPStatus
from json import JSONDecodeError
from typing import Self, Any

import httpx
from httpx import Auth

from marketplace_apis import __version__

try:
    from orjson import loads

    loads_func = loads
except ModuleNotFoundError:
    from json import loads

    loads_func = loads


class ApiRequestException(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(f"API Request failed with status {status_code}: {message}")


class AsyncRequester:
    """
    Class for making requests to some API asynchronously. Usually this gets subclassed.
    Attributes:
        endpoint (str): The base URL for the API.
        headers (dict): Headers to send with every request.
        auth (Auth): Authentication credentials.
        _http_client (httpx.AsyncClient): The HTTP client used to make requests.
    """

    @staticmethod
    async def check_for_errors(func, self, *args, **kwargs):
        response_, data = await func(self, *args, **kwargs)
        if response_.status_code != HTTPStatus.OK:
            raise ApiRequestException(response_.status_code, response_.text)
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
        headers: dict[str, str] | None = None,
        auth: Auth | None = None,
    ):
        self.headers = headers if headers else {}
        self.endpoint = endpoint
        self._auth = auth
        self.headers["User-Agent"] = f"MarketplaceApis/{__version__}"
        self._http_client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> Self:
        self._http_client = httpx.AsyncClient(
            headers=self.headers, base_url=self.endpoint, auth=self._auth
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._http_client.aclose()

    @_check_for_errors_decorator
    async def _make_request(
        self,
        method: str,
        path: str,
        params: dict[str, str] | None = None,
        data: dict[str, Any] = None,
        decode: bool = True,
    ) -> tuple[httpx.Response, dict | bytes]:
        params = params if params else {}
        kwargs = {"params": params}
        if data:
            kwargs |= {"json": data}
        response = await getattr(self._http_client, method)(path, **kwargs)
        decoded = response.content
        if decode:
            with contextlib.suppress(JSONDecodeError):
                decoded = loads_func(decoded)
        return response, decoded

    async def get(
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
        return await self._make_request("get", path, params, decode=decode)

    async def post(
        self,
        path: str,
        data: dict[str, Any] | None = None,
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
        return await self._make_request("post", path, params, data, decode=decode)


if __name__ == "__main__":
    from pathlib import Path

    async def async_function():
        requester = AsyncRequester(
            "https://cataas.com/",
        )

        async def get_cat(client, i):
            print(f"start {i}")  # noqa: T201
            _, content = await client.get("cat", decode=False)
            print(f"end {i}")  # noqa: T201
            with Path.open(f"test{i}.png", "wb") as f:
                f.write(content)

        async with requester.client() as client, asyncio.TaskGroup() as tg:
            for i in range(10):
                tg.create_task(get_cat(client, i))

    asyncio.run(async_function())
