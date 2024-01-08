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

from dataclasses import dataclass

from marketplace_apis.yandex.campaign.enums import CampaignSettingsScheduleSourceType
from marketplace_apis.yandex.campaign.settings_delivery import CampaignSettingsDelivery
from marketplace_apis.yandex.common.region import Region


@dataclass
class CampaignSettingsLocalRegion(Region):
    """Информация о своем регионе магазина."""

    deliveryOptionsSource: CampaignSettingsScheduleSourceType
    """Источник информации о расписании работы службы доставки."""
    delivery: CampaignSettingsDelivery
    """Информация о доставке в своем регионе магазина."""
