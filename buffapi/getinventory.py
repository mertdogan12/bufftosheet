import time
import requests
import os
import json


class Item:
    item_id: int
    name: str
    new: bool | None
    pic_url: str

    def __init__(self, item_id: int, name: str, new: bool | None, pic_url: str) -> None:
        self.item_id = item_id
        self.name = name
        self.new = new
        self.pic_url = pic_url


class Inventory:
    total_ammount = 0.0
    sold_ammount = 0.0
    total_page = 0
    items: list[Item] = []


def getinv():
    wait_time = 20

    inv = Inventory()
    inv = inv_addpage(inv, 1)
    if inv is None:
        return None

    for i in range(2, inv.total_page + 1):
        print(f"Waiting {wait_time}sec")
        time.sleep(wait_time)

        inv = inv_addpage(inv, i)
        if inv is None:
            return None

    return inv


def inv_addpage(inv: Inventory, page: int):
    cookies = {
        'Locale-Supported': 'en',
        'game': 'csgo',
        'session': os.getenv("SESSION"),
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest', 'DNT': '1', 'Referer': 'https://buff.163.com/market/steam_inventory?game=csgo',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    params = {
        'game': 'csgo',
        'force': '0',
        'page_num': str(page),
        'page_size': '50',
        'search': '',
        'state': 'all',
    }

    response = requests.get('https://buff.163.com/api/market/steam_inventory',
                            params=params, cookies=cookies, headers=headers)

    if response.status_code != 200:
        print(
            f"Got status code {response.status_code} while getting the inventory")
        return None

    try:
        data = response.json()["data"]

        inv.total_ammount = float(data["total_amount"])
        inv.total_page = int(data["total_page"])

        for item in data["items"]:
            itemid = int(item["goods_id"])
            name = str(item["name"])
            pic_url = str(item["icon_url"])

            inv.items.append(Item(
                item_id=itemid,
                name=name,
                new=None,
                pic_url=pic_url,
            ))

        print(f"Got the inventory page {page}/{inv.total_page}")
        return inv

    except (KeyError, IndexError):
        print("Error while getting the data from the inventory")
        print(json.dumps(response.json(), indent=4))
        return None
