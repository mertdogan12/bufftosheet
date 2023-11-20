import json
import sys
import time

import proxies
from .getinventory import Item


class ItemPrice:
    price = 0.0
    new = False

    def __init__(self, price: float, new: bool) -> None:
        self.price = price
        self.new = new


def getitemprices(items: list[Item], proxies: list[proxies.Proxy]):
    item_pos = 0
    item_prices: list[ItemPrice] = []
    wait_time = 60

    while item_pos < len(items):
        for proxy in proxies:
            if item_pos >= len(items):
                break

            item = items[item_pos]

            item_price = getitemprice(item.item_id, proxy)
            item_pos += 1

            if not item_price:
                items.append(item)
                continue

            if item.new is None:
                print(f"Error: item.new is {item.new}")
                sys.exit()

            item_prices.append(ItemPrice(item_price, item.new))
            print(
                f"Got the itemprice from the item {item.name}: {item_price}¥ ({item_pos}/{len(items)})")

        print(f"Waiting {wait_time}sec")
        time.sleep(wait_time)

    return item_prices


def getitemprice(id: int, proxy: proxies.Proxy):
    cookies = {
        'Locale-Supported': 'en',
        'game': 'csgo',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Referer': 'https://buff.163.com/goods/%s?from=market' % id,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    params = {
        'game': 'csgo',
        'goods_id': str(id),
        'page_num': '1',
        'sort_by': 'default',
        'mode': '',
        'allow_tradable_cooldown': '1',
    }

    response = proxies.request_proxy('https://buff.163.com/api/market/goods/sell_order',
                                     params=params, cookies=cookies, headers=headers, proxy=proxy)

    if response.status_code != 200:
        print(
            f"Got status code {response.status_code} while getting the price from the item with the id {id}")
        return None

    try:
        data = response.json()["data"]

        if len(data["items"]) == 0:
            return 0.0

        price = float(data["items"][0]["price"])

        return price

    except (KeyError, IndexError):
        print(f"Error while getting the data from the item with the id {id}")
        print("Json: " + json.dumps(response.json(), indent=4))
        return None
