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
from typing import Unpack

from marketplace_apis.ozon.common.abc_methods import SellerApiABCMethods
from marketplace_apis.ozon.delivery_method.delivery_method import DeliveryMethod
from marketplace_apis.ozon.delivery_method.methods_types import (
    ListDeliveryMethodsFilter,
)
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.utils import kwargs_to_filters


class DeliveryMethodMethods(SellerApiABCMethods):
    async def list_delivery_methods(
        self,
        iter_: bool = True,
        limit: int = 1000,
        offset: int = 0,
        **kwargs: Unpack[ListDeliveryMethodsFilter],
    ) -> list[DeliveryMethod]:
        """
        Получить список методов доставки.
        # Аргументы:
        * iter_ (по умолчанию True) - необходимо ли получать все объекты,
        итерируясь по страницам
        * limit (по умолчанию 1000) - максимальное количество объектов, которое будет
        получено за один запрос
        * offset (по умолчанию 0) - с какого объекта начать первую страницу?
        * filter_provider_id (опционально) - Идентификатор службы доставки (int).
        * filter_status (опционально) - Идентификатор службы доставки
        ([DeliveryMethodStatus](enums.md#ozon.delivery_method.enums.DeliveryMethodStatus)).
        * filter_warehouse_id (опционально) - Идентификатор склада (int).
        # Возвращает: list[[DeliveryMethod](delivery_method.md)]
        """
        raw_delivery_methods = []
        filter_, _ = kwargs_to_filters(kwargs)

        async def make_request():
            resp, decoded_resp = await self.client.post(
                API_PATH["list_delivery_methods"],
                data={
                    "limit": limit,
                    "offset": offset,
                    "filter": filter_,
                },
            )
            nonlocal raw_delivery_methods
            raw_delivery_methods += decoded_resp["result"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["has_next"]:
            offset += limit
            _, data = await make_request()

        return [
            DeliveryMethod.from_dict(raw_delivery_method)
            for raw_delivery_method in raw_delivery_methods
        ]
