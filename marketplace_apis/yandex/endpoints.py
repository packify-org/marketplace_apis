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
API_PATH = {
    # region campaign
    "list_campaigns": "campaigns/",
    "get_campaign_by_id": "campaigns/",
    "get_campaign_logins": "campaigns/",
    "get_campaign_settings": "campaigns/",
    "get_campaign_by_login": "campaigns/by_login/",
    # endregion
    # region offers
    "list_offer_mappings": "offer-mappings",
    # endregion
    # region warehouse
    "list_fby_warehouses": "https://api.partner.market.yandex.ru/warehouses",
    "list_warehouses": "warehouses",
    # endregion
    # region orders
    "list_orders": "orders",
    "get_order_by_number": "orders",
    "get_delivery_labels": "delivery/labels",
    # endregion
    # region oauth
    "oauth_token": "https://oauth.yandex.ru/token",
    # endregion
}
