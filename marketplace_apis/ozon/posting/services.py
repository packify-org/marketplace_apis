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

from marketplace_apis.ozon.base import SellerApiBaseModel


@dataclass
class Services(SellerApiBaseModel):
    """Услуги по обработке отправления."""

    marketplace_service_item_deliv_to_customer: float
    """Последняя миля."""
    marketplace_service_item_direct_flow_trans: float
    """Магистраль."""
    marketplace_service_item_dropoff_ff: float
    """Обработка отправления на фулфилмент складе (ФФ)."""
    marketplace_service_item_dropoff_pvz: float
    """Обработка отправления в ПВЗ."""
    marketplace_service_item_dropoff_sc: float
    """Обработка отправления в сортировочном центре."""
    marketplace_service_item_fulfillment: float
    """Сборка заказа."""
    marketplace_service_item_pickup: float
    """Выезд транспортного средства по адресу продавца
     для забора отправлений (Pick-up)."""
    marketplace_service_item_return_after_deliv_to_customer: float
    """Обработка возврата."""
    marketplace_service_item_return_flow_trans: float
    """Обратная магистраль."""
    marketplace_service_item_return_not_deliv_to_customer: float
    """Обработка отмен."""
    marketplace_service_item_return_part_goods_customer: float
    """Обработка невыкупа."""
