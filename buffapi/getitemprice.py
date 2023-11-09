import requests
import json

cookies = {
    'Locale-Supported': 'en',
    'game': 'csgo',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Referer': 'https://buff.163.com/goods/763236?from=market',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
}

params = {
    'game': 'csgo',
    'goods_id': '763236',
    'page_num': '1',
    'sort_by': 'default',
    'mode': '',
    'allow_tradable_cooldown': '1',
}

response = requests.get('https://buff.163.com/api/market/goods/sell_order',
                        params=params, cookies=cookies, headers=headers)

response.raise_for_status()

print(json.dumps(response.json(), indent=4))
