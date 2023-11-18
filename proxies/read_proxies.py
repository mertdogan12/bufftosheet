import os


class Proxy:
    def __init__(self, address: str,
                 name: str | None, password: str | None) -> None:
        self.address = address
        self.name = name
        self.password = password


def read_proxies():
    proxy_file = open(os.getenv("PROXYFILE") or "./proxies.txt")

    proxies = []

    for line in proxy_file.readlines():
        l = line.split(':')

        address = ':'.join(l[:2])
        name = None
        password = None

        if len(l) == 4:
            name = l[2]
            password = l[3]

        proxies.append(Proxy(address, name, password))

    print(f"Found {len(proxies)} proxies")

    return proxies
