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
from pathlib import Path

import pytest

from marketplace_apis.ozon.seller_api import SellerApi


@pytest.fixture(scope="module")
def auth_data() -> list[str, str]:
    data = {}
    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                data[k] = v.strip("\n")
    return data["API_KEY"], data["CLIENT_ID"]


@pytest.fixture(scope="module")
def seller_api(auth_data) -> SellerApi:
    return SellerApi(*auth_data)


class ValueStorage:
    postings = None
    product = None
