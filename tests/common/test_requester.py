# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (C) 2024  Anatoly Raev
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

import httpx
import pytest
from httpx import Response

from marketplace_apis.common.requester import AsyncRequester, ApiRequestException
from marketplace_apis import __version__


@pytest.fixture()
def requester_no_headers() -> AsyncRequester:
    return AsyncRequester("https://foo.bar/")


def header_echo(request):
    return Response(200, json={"headers": dict(request.headers)})


def body_echo(request):
    return Response(200, content=request.content)


def urlparams_echo(request: httpx.Request):
    return Response(200, json={"params": dict(request.url.params)})


@pytest.mark.respx(base_url="https://foo.bar")
@pytest.mark.asyncio
class TestRequester:
    class TestGet:
        async def test_get_200(self, requester_no_headers: AsyncRequester, respx_mock):
            respx_mock.get("get").mock(return_value=httpx.Response(200))
            async with requester_no_headers as client:
                response, decoded = await client.get("get")
                assert response.status_code == HTTPStatus.OK

        async def test_get_401(self, requester_no_headers: AsyncRequester, respx_mock):
            respx_mock.get("status/401").mock(return_value=httpx.Response(401))
            async with requester_no_headers as client:
                with pytest.raises(ApiRequestException):
                    response, decoded = await client.get("status/401")

        async def test_get_headers(self, respx_mock):
            respx_mock.get("headers").mock(side_effect=header_echo)
            async with AsyncRequester(
                "https://foo.bar/", headers={"test-header": "test"}
            ) as client:
                response, decoded = await client.get("headers")
                assert decoded["headers"]["test-header"] == "test"
                # test user-agent header
                assert "MarketplaceApis" in decoded["headers"]["user-agent"]
                assert __version__ in decoded["headers"]["user-agent"]

    class TestPost:
        async def test_post_200(self, requester_no_headers: AsyncRequester, respx_mock):
            respx_mock.post("post").mock(return_value=httpx.Response(200))
            async with requester_no_headers as client:
                response, decoded = await client.post("post")
                assert response.status_code == HTTPStatus.OK

        async def test_post_401(self, requester_no_headers: AsyncRequester, respx_mock):
            respx_mock.post("status/401").mock(return_value=httpx.Response(401))
            async with requester_no_headers as client:
                with pytest.raises(ApiRequestException):
                    response, decoded = await client.post("status/401")

        async def test_post_data(
            self, requester_no_headers: AsyncRequester, respx_mock
        ):
            respx_mock.post("post").mock(side_effect=body_echo)
            async with requester_no_headers as client:
                response, decoded = await client.post(
                    "post", data={"test": ["test1", "test2"]}
                )
                assert decoded["test"] == ["test1", "test2"]

        async def test_post_params(
            self, requester_no_headers: AsyncRequester, respx_mock
        ):
            respx_mock.post("post").mock(side_effect=urlparams_echo)
            async with requester_no_headers as client:
                response, decoded = await client.post("post", params={"test": "true"})
                assert decoded["params"]["test"] == "true"

        async def test_post_headers(self, respx_mock):
            respx_mock.post("headers").mock(side_effect=header_echo)
            async with AsyncRequester(
                "https://foo.bar/", headers={"test-header": "test"}
            ) as client:
                response, decoded = await client.post("headers")
                assert decoded["headers"]["test-header"] == "test"
                # test user-agent header
                assert "MarketplaceApis" in decoded["headers"]["user-agent"]
                assert __version__ in decoded["headers"]["user-agent"]
