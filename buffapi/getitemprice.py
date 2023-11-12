import requests
import json


def getitemprices(ids: list[str]):
    return [getitemprice(id) for id in ids]


def getitemprice(id: str):
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
        'goods_id': id,
        'page_num': '1',
        'sort_by': 'default',
        'mode': '',
        'allow_tradable_cooldown': '1',
    }

    response = requests.get('https://buff.163.com/api/market/goods/sell_order',
                            params=params, cookies=cookies, headers=headers)

    if response.status_code != 200:
        print("Got status code %d while getting the price from the item with the id %s" % (
            response.status_code, id))
        return None

    try:
        data = response.json()["data"]
        price = float(data["items"][0]["price"])

        print("Got itemprice from id %s: %f" % (id, price))
        return price

    except (KeyError, IndexError):
        print("Error while getting the data from the item with the id " + id)
        print("Json: " + json.dumps(response.json(), indent=4))
        return None
