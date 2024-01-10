# MarkeplaceApis

Easy way to communicate with russian marketplaces!

## Features:

* Fully async
* Uses httpx and mashumaro - blazing fast!
* Easy and not verbose to use
* Supports Ozon SellerAPI and Yandex MarketAPI - support for Wildberries API planned

## Installation

```
pip install "marketplace_apis @ git+https://github.com/packify-org/marketplace_apis.git"
# or to install library with ORJSON 
pip install "marketplace_apis[orjson] @ git+https://github.com/packify-org/marketplace_apis.git"
```

## Usage example

> [!WARNING]
> Do not use one SellerApi or MarketApi instance in multiple with context managers

### Ozon SellerAPI

```python
import asyncio
from datetime import datetime, timedelta
from marketplace_apis.ozon.seller_api import SellerApi
import os


async def main():
    async with SellerApi(os.getenv("API_KEY"), os.getenv("CLIENT_ID")) as client:
        # print all postings from 14 days before now to now:
        now = datetime.now()
        postings = await client.posting.list_postings(
            filter_since=now - timedelta(14),
            filter_to=now)
        print(postings)
        # get product infos and attributes from first posting products concurrently
        async with asyncio.TaskGroup() as tg:
            posting = postings[0]
            offer_ids = [product.offer_id for product in posting.products]
            info = tg.create_task(client.product.list_info(["112026854"]))
            attributes = tg.create_task(
                client.product.list_attributes(offer_id=["112026854"]))
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
    # you don't have to pass campaign_id or business_id,
    # if you will not use methods, that require them
    async with MarketApi(os.getenv("TOKEN"), os.getenv("CAMPAIGN_ID"),
                         os.getenv("BUSINESS_ID")) as client:
        # print all orders from 14 days before now to now:
        now = datetime.now()
        orders = await client.order.list_orders(
            fromDate=(now - timedelta(14)).date(),
            toDate=now.date())
        print(orders)
        # get offer_mappings of first order items
        order = orders[0]
        offer_ids = [item.offerId for item in order.items]
        offer_mappings = await client.offer_mapping.list_offer_mappings(
            offerIds=offer_ids)
        print(offer_mappings)


asyncio.run(main())
```

## Currently supported api endpoints:

#### OZON SellerAPI

Supports endpoints for:

* delivery methods,
* warehouse,
* posting,
* product.

#### Yandex MarketAPI

Supports endpoints for:

* order,
* campaign,
* warehouse,
* oauth.
