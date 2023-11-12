import requests
import sys

from proxies.read_proxies import Proxy


def test_proxies(proxies: list[Proxy]):
    working = []

    print("Testing proxies")

    for proxy in proxies:
        proxy_server = {
            'http': 'http://' + proxy.address
        }

        try:
            if proxy.name is None or proxy.password is None:
                requests.get("http://google.com", proxies=proxy_server)
            else:
                auth = (proxy.name, proxy.address)
                requests.get("http://google.com",
                             proxies=proxy_server, auth=auth)

        except KeyboardInterrupt:
            sys.exit(0)

        except:
            print(proxy.address + " not working")
            continue

        else:
            print(proxy.address + " works")
            working.append(proxy)

    return working
