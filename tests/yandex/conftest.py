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

from marketplace_apis.yandex.market_api import MarketApi


@pytest.fixture(scope="module")
def auth_data() -> list[str, str, str]:
    data = {}
    with Path.open(".env", "r") as f:
        for line in f.readlines():
            if line:
                k, v = line.split("=")
                data[k] = v.strip("\n")
    return data["TOKEN"], data["CAMPAIGN_ID"], data["BUSINESS_ID"]


@pytest.fixture(scope="module")
def market_api(auth_data) -> MarketApi:
    return MarketApi(*auth_data)


class ValueStorage:
    campaigns = None
    campaign = None
    campaign_logins = None
