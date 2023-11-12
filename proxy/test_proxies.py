import requests


def test_proxies(proxies: list[str]):
    working = []

    print("Testing proxies")

    for proxy in proxies:
        proxy_server = {
            'http': 'http://' + proxy
        }

        try:
            requests.get("http://google.com", proxies=proxy_server)
        except:
            continue
        else:
            print(proxy + " works")
            working.append(proxy)

    return working
