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

from marketplace_apis.common.utils import dict_datetime_to_iso
from marketplace_apis.ozon.common.abc_methods import SellerApiABCMethods
from marketplace_apis.ozon.endpoints import API_PATH
from marketplace_apis.ozon.posting.label import AsyncLabelGetResult
from marketplace_apis.ozon.posting.methods_types import (
    ListPostings,
    GetPostingsWith,
    ShipPostingWith,
    ShipPostingProduct,
)
from marketplace_apis.ozon.posting.posting import Posting
from marketplace_apis.ozon.posting.ship import PostingShipResult
from marketplace_apis.ozon.utils import kwargs_to_filters


class PostingMethods(SellerApiABCMethods):
    async def list_postings(
        self,
        dir_: str = "desc",
        iter_: bool = True,
        limit: int = 1000,
        offset: int = 0,
        **kwargs: Unpack[ListPostings],
    ) -> list[Posting]:
        """
        Получить список отправлений.
        # Аргументы:
        * filter_since - Дата начала периода, за который нужно получить список
        отправлений. (datetime)
        * filter_to - Дата конца периода, за который нужно получить список
        отправлений. (datetime)
        * dir_ (по умолчанию "desc") - направление сортировки
        * iter_ (по умолчанию True) - необходимо ли получать все объекты,
        итерируясь по страницам
        * limit (по умолчанию 1000) - максимальное количество объектов, которое будет
        получено за один запрос
        * offset (по умолчанию 0) - с какого объекта начать первую страницу?
        * with_analytics_data (опционально) - Добавить в ответ данные аналитики.
        * with_barcodes (опционально) - Добавить в ответ штрихкоды отправления.
        * with_financial_data (опционально) - Добавить в ответ финансовые данные.
        * with_translit (опционально) - Выполнить транслитерацию возвращаемых значений.
        * filter_delivery_method_id (опционально) - Идентификатор способа доставки.
        (list[int])
        * filter_order_id (опционально) - Идентификатор заказа. (int)
        * filter_provider_id (опционально) - Идентификатор службы доставки. (list[int])
        * filter_status (опционально) - Статус отправления.
        ([PostingStatus](enums.md#ozon.posting.enums.PostingStatus))
        * filter_warehouse_id (опционально) - Идентификатор службы доставки. (list[int])

        # Возвращает: list[[Posting](posting.md)]
        """
        dict_datetime_to_iso(kwargs)
        raw_postings = []
        filter_, with_ = kwargs_to_filters(kwargs)

        async def make_request():
            resp, decoded_resp = await self.client.post(
                API_PATH["list_postings"],
                data={
                    "limit": limit,
                    "offset": offset,
                    "dir": dir_,
                    "filter": filter_,
                    "with": with_,
                },
            )
            nonlocal raw_postings
            raw_postings += decoded_resp["result"]["postings"]
            return resp, decoded_resp

        _, data = await make_request()
        while iter_ and data["result"]["has_next"]:
            offset += limit
            _, data = await make_request()

        return [Posting.from_dict(raw_posting) for raw_posting in raw_postings]

    async def get_by_number(
        self, posting_number: str, **kwargs: Unpack[GetPostingsWith]
    ) -> Posting:
        """
        Получить отправление по его номеру.
        # Аргументы:
        * posting_number - номер отправления
        * product_exemplars (опционально) - Добавить в ответ данные о продуктах и их
        экземплярах.
        * related_postings (опционально) - Добавить в ответ номера связанных
        отправлений. Связанные отправления — те, на которое было разделено родительское
        отправление при сборке.

        # Возвращает: [Posting](posting.md)
        """
        _, with_ = kwargs_to_filters(kwargs)
        _, data = await self.client.post(
            API_PATH["get_posting_by_number"],
            data={"posting_number": posting_number, "with": with_},
        )
        return Posting.from_dict(data["result"])

    async def label_task_create(self, posting_numbers: list[str]) -> int:
        """
        Создать задание на асинхронное получение этикетки.
        # Аргументы:
        * posting_number - номер отправления

        # Возвращает: int - Идентификатор задания на формирование этикеток.
        """
        _, data = await self.client.post(
            API_PATH["package_label_create"], data={"posting_number": posting_numbers}
        )
        return data["result"]["task_id"]

    async def label_task_get(self, task_id: int) -> AsyncLabelGetResult:
        """
        Проверить статус задания или получить этикетку, созданную label_task_create
        # Аргументы:
        * task_id - Идентификатор задания на формирование этикеток.

        # Возвращает:
        [AsyncLabelGetResult](label.md#ozon.posting.label.AsyncLabelGetResult)
        """
        _, data = await self.client.post(
            API_PATH["package_label_get"], data={"task_id": task_id}
        )
        return AsyncLabelGetResult.from_dict(data["result"])

    async def ship(
        self,
        posting_number,
        packages: list[list[ShipPostingProduct]],
        **kwargs: Unpack[ShipPostingWith],
    ) -> PostingShipResult:
        """
        Собрать заказ.
        # Аргументы:
        * posting_number - номер отправления
        * packages - список упаковок. Каждая упаковка - список товаров.
        (list[list[[ShipPostingProduct]
        (methods_types.md#ozon.posting.methods_types.ShipPostingProduct)]])
        * with_additional_data (опционально) - Добавить в ответ дополнительную
        информацию.

        # Возвращает: [PostingShipResult](ship.md#ozon.posting.ship.PostingShipResult)
        """
        _, with_ = kwargs_to_filters(kwargs)
        _, data = await self.client.post(
            API_PATH["ship_posting"],
            data={
                "posting_number": posting_number,
                "with": with_,
                "packages": [{"products": products} for products in packages],
            },
        )
        return PostingShipResult.from_dict(data)
