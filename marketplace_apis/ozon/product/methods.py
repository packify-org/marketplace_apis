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
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.product.methods_types import ListAttributesFilter
from marketplace_apis.ozon.product.product import Product


class ProductMethods(SellerApiABCMethods):
    async def list_info(
        self,
        offer_id: list[str] | None = None,
        product_id: list[int] | None = None,
        sku: list[int] | None = None,
        raw: bool = False,
    ) -> list[Product]:
        """
        Получить список информации о товарах.
        # Аргументы:
        * offer_id - (опционально) список offer_id, по которым требуется получить
        информацию (list[str])
        * product_id - (опционально)  список product_id, по которым требуется получить
        информацию (list[int])
        * sku - (опционально) список sku,  по которым требуется получить информацию
        (list[int])

        # Возвращает: list[[Product](product.md)]
        """
        _, data = await self.client.post(
            API_PATH["list_product_info"],
            data={
                "offer_id": offer_id,
                "product_id": product_id,
                "sku": sku,
            },
        )
        if raw == True:
            return data["result"]["items"]
        return [
            Product.from_dict(raw_product) for raw_product in data["result"]["items"]
        ]


    async def list_attributes(
        self,
        iter_: bool = True,
        limit: int = 1000,
        dir_="DESC",
        raw: bool = False,
        **kwargs: Unpack[ListAttributesFilter],
    ) -> list[Product]:
        """
        Получить список аттрибутов товара.
        # Аргументы:
        * dir_ (по умолчанию "desc") - направление сортировки
        * iter_ (по умолчанию True) - необходимо ли получать все объекты,
        итерируясь по страницам
        * limit (по умолчанию 1000) - максимальное количество объектов, которое будет
        получено за один запрос
        * offer_id (опционально) - Фильтр по параметру offer_id.
        Можно передавать список значений.
        * product_id (опционально) - Фильтр по параметру product_id.
        Можно передавать список значений.
        * visibility (опционально - Фильтр по видимости товара
        ([Visibility](enums.md#ozon.product.enums.Visibility)

        # Возвращает: list[[Product](product.md)]
        """

        raw_products = []

        async def make_request(last_id=None):
            resp, decoded_resp = await self.client.post(
                API_PATH["list_product_attributes"],
                data={
                    "limit": limit,
                    "sort_dir": dir_,
                    "filter": kwargs,
                }
                | ({"last_id": last_id} if last_id else {}),
            )
            nonlocal raw_products
            raw_products += decoded_resp["result"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["last_id"]:
            _, data = await make_request(data["last_id"])

        if raw == True:
            return raw_products
        return [Product.from_dict(raw_product) for raw_product in raw_products]
    

    async def list_product(
        self,
        iter_: bool = True,
        limit: int = 1000,
        raw: bool = False,
        **kwargs: Unpack[ListAttributesFilter],
    ) -> list[Product]:
        """
        Получить список товаров селлера. Если не указывать критерии фильтрации,
        будут получены все товары селлера.
        # Аргументы:
        * iter_ (по умолчанию True) - необходимо ли получать все объекты,
        итерируясь по страницам
        * limit (по умолчанию 1000) - максимальное количество объектов, которое будет
        получено за один запрос
        * offer_id (опционально) - Фильтр по параметру offer_id.
        Можно передавать список значений.
        * product_id (опционально) - Фильтр по параметру product_id.
        Можно передавать список значений.
        * visibility (опционально - Фильтр по видимости товара
        ([Visibility](enums.md#ozon.product.enums.Visibility)
        """
        
        raw_products = []

        async def make_request(last_id=None):
            resp, decoded_resp = await self.client.post(
                API_PATH["list_product"],
                data={
                    "limit": limit,
                    "filter": kwargs,
                }
                | ({"last_id": last_id} if last_id else {}),
            )
            nonlocal raw_products
            raw_products += decoded_resp["result"]['items']
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["result"]["last_id"]:
            _, data = await make_request(data["result"]["last_id"])

        if raw == True:
            return raw_products
        raise NotImplementedError(f" Для данного метода предусмотрена выгрузка только сырых" 
                                  f" данных, используйте аттрибут raw=True") 
