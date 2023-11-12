import requests
import os
import json


class Item:
    item_id = 0
    name = ""
    price = 0.0

    def __init__(self, item_id: int, name: str, price: float) -> None:
        self.item_id = item_id
        self.name = name
        self.price = price


class Inventory:
    total_ammount = 0.0
    items: list[Item] = []

    def __init__(self, total_amount: float, items: list[Item]) -> None:
        self.total_ammount = total_amount
        self.items = items


def getinv():
    cookies = {
        'Locale-Supported': 'en',
        'game': 'csgo',
        'session': os.getenv("SESSION"),
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Referer': 'https://buff.163.com/market/steam_inventory?game=csgo',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    params = {
        'game': 'csgo',
        'force': '0',
        'page_num': '1',
        'page_size': '50',
        'search': '',
        'state': 'all',
    }

    response = requests.get('https://buff.163.com/api/market/steam_inventory',
                            params=params, cookies=cookies, headers=headers)

    if response.status_code != 200:
        print("Got status code %d while getting the inventory")
        return None

    try:
        data = response.json()["data"]

        total_ammount = float(data["total_amount"])
        items: list[Item] = []

        for item in data["items"]:
            itemid = int(item["goods_id"])
            name = str(item["name"])
            price = float(item["sell_min_price"])

            items.append(Item(itemid, name, price))

        return Inventory(total_ammount, items)

    except (KeyError, IndexError):
        print("Error while getting the data from the inventory")
        print(json.dumps(response.json(), indent=4))
        return None
    except TimeoutError:
        print("Connection timeout while getting the data from the inventory")
        return None
