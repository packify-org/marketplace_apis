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
from urllib.parse import urljoin

from marketplace_apis.common.base import ABCMethods
from marketplace_apis.common.requester import Requester
from marketplace_apis.yandex.campaigns.campaign import Campaign
from marketplace_apis.yandex.campaigns.settings import CampaignSettings
from marketplace_apis.yandex.endpoints import API_PATH


class CampaignMethods(ABCMethods):
    def __init__(self, requester: Requester):
        super().__init__(requester)

    def list_campaigns(
        self,
        iter_: bool = True,
        page_size: int = 50,
        page: int = 1,
    ) -> list[Campaign]:
        """List campaigns.
        :param page_size: Maximum amount of campaigns what will be retrieved in one
        request
        :param page: page from that campaigns will be retrieved
        :param iter_: Whenever to get all postings by making multiple requests or not

        :return: List of campaigns
        """
        raw_campaigns = []

        def make_request():
            resp, decoded_resp = self._requester.get(
                API_PATH["list_campaigns"],
                params={"pageSize": page_size, "page": page},
            )
            nonlocal raw_campaigns
            raw_campaigns += decoded_resp["campaigns"]
            return resp, decoded_resp

        _, data = make_request()
        while iter_ and data["pager"]["pagesCount"] != data["pager"]["currentPage"]:
            page += 1
            _, data = make_request()

        return [Campaign.from_dict(raw_campaign) for raw_campaign in raw_campaigns]

    def get_by_id(self, campaign_id: int) -> Campaign:
        _, data = self._requester.get(
            urljoin(API_PATH["get_campaign_by_id"], str(campaign_id))
        )
        return Campaign.from_dict(data["campaign"])

    def get_settings(self, campaign_id: int) -> Campaign:
        _, data = self._requester.get(
            urljoin(API_PATH["get_campaign_settings"], f"{campaign_id}/settings")
        )
        return CampaignSettings.from_dict(data["settings"])

    def get_logins(self, campaign_id: int) -> list[str]:
        _, data = self._requester.get(
            urljoin(API_PATH["get_campaign_logins"], f"{campaign_id}/logins")
        )
        return data

    def get_by_login(
        self, login: str, iter_: bool = True, page_size: int = 50, page: int = 1
    ) -> list[str]:
        raw_campaigns = []

        def make_request():
            resp, decoded_resp = self._requester.get(
                urljoin(API_PATH["get_campaign_by_login"], f"by_login/{login}"),
                params={"pageSize": page, "page": page_size},
            )
            nonlocal raw_campaigns
            raw_campaigns += decoded_resp["campaigns"]
            return resp, decoded_resp

        _, data = make_request()
        while iter_ and data["pager"]["pagesCount"] != data["pager"]["currentPage"]:
            page += 1
            _, data = make_request()

        return [Campaign.from_dict(raw_campaign) for raw_campaign in raw_campaigns]
