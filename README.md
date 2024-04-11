# marketplace_apis

Простой способ общаться с российскими маркетплейсами!

* Полностью асинхронная библиотека
* Простая и понятная в использовании
* Поддерживает Ozon SellerAPI и Yandex MarketAPI - поддержка Wildberries API soon™
* Использует httpx и mashumaro под капотом

Подробная документация по ссылке https://packify-org.github.io/marketplace_apis/


# Примеры использования

### Ozon SellerAPI

```python
import asyncio
from datetime import datetime, timedelta
from marketplace_apis.ozon.seller_api import SellerApi
import os


async def main():
    async with SellerApi(os.getenv("API_KEY"), os.getenv("CLIENT_ID")) as client:
        # получить все отправления за прошедшие 14 дней
        now = datetime.now()
        postings = await client.posting.list_postings(
            filter_since=now - timedelta(14),
            filter_to=now)
        print(postings)
        # получить информацию и товарах в первом отправлении
        async with asyncio.TaskGroup() as tg:
            posting = postings[0]
            offer_ids = [product.offer_id for product in posting.products]
            info = tg.create_task(client.product.list_info(offer_ids))
            attributes = tg.create_task(
                client.product.list_attributes(offer_id=offer_ids))
        print(info.result(), attributes.result())


asyncio.run(main())
```

### Yandex MarketAPI

```python
import asyncio
from datetime import datetime, timedelta
from marketplace_apis.yandex.market_api import MarketApi
import os


async def main():
    # не нужно передавать CAMPAIGN_ID или BUSINESS_ID,
    # если вы не будете использовать методы, которым они нужны
    async with MarketApi(os.getenv("TOKEN"), os.getenv("CAMPAIGN_ID"),
                         os.getenv("BUSINESS_ID")) as client:
        # получить все отправления за прошедшие 14 дней
        now = datetime.now()
        orders = await client.order.list_orders(
            fromDate=(now - timedelta(14)).date(),
            toDate=now.date())
        print(orders)
        # получить offer_mappings из первого отправления
        order = orders[0]
        offer_ids = [item.offerId for item in order.items]
        offer_mappings = await client.offer_mapping.list_offer_mappings(
            offerIds=offer_ids)
        print(offer_mappings)


asyncio.run(main())
```
