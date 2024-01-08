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
import pytest

from marketplace_apis.yandex.campaign.campaign import Campaign
from marketplace_apis.yandex.campaign.settings import CampaignSettings
from tests.yandex.conftest import ValueStorage


@pytest.mark.asyncio
class TestCampaign:
    async def test_list_campaigns(self, market_api):
        async with market_api as client:
            campaigns = await client.campaign.list_campaigns()
            ValueStorage.campaigns = campaigns
            assert isinstance(campaigns, list)
            assert isinstance(campaigns[0], Campaign)

    async def test_get_by_id(self, market_api):
        async with market_api as client:
            campaign = await client.campaign.get_by_id(ValueStorage.campaigns[0].id_)
            ValueStorage.campaign = campaign
            assert isinstance(campaign, Campaign)

    async def test_get_settings(self, market_api):
        async with market_api as client:
            settings = await client.campaign.get_settings(ValueStorage.campaign.id_)
            assert isinstance(settings, CampaignSettings)

    async def test_get_logins(self, market_api):
        async with market_api as client:
            logins = await client.campaign.get_logins(ValueStorage.campaign.id_)
            ValueStorage.campaign_logins = logins
            assert isinstance(logins, list)

    async def test_get_by_login(self, market_api):
        async with market_api as client:
            campaigns = await client.campaign.get_by_login(
                ValueStorage.campaign_logins[0]
            )
            assert isinstance(campaigns, list)
            assert isinstance(campaigns[0], Campaign)
