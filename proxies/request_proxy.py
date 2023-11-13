import requests
from proxies.read_proxies import Proxy


def request_proxy(url: str, params, cookies, headers, proxy: Proxy):
    proxy_server = {
        'http': 'http://' + proxy.address
    }

    if proxy.name is None or proxy.password is None:
        return requests.get(url, params=params, cookies=cookies,
                            headers=headers, proxies=proxy_server)
    else:
        auth = (proxy.name, proxy.address)
        return requests.get(url, params=params, cookies=cookies,
                            headers=headers, proxies=proxy_server, auth=auth)
