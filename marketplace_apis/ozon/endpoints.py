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
    # region postings
    "list_postings": "v3/posting/fbs/list",
    "get_posting_by_number": "v3/posting/fbs/get",
    "ship_posting": "v4/posting/fbs/ship",
    "package_label_create": "v1/posting/fbs/package-label/create",
    "package_label_get": "v1/posting/fbs/package-label/get",
    # endregion
    # region warehouses
    "list_warehouses": "v1/warehouse/list",
    # endregion
    # region delivery methods
    "list_delivery_methods": "v1/delivery-method/list",
    # endregion
    # region products
    "list_product_info": "v2/product/info/list",
    # endregion
}
