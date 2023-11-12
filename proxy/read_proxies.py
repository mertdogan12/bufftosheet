import os


def read_proxies():
    proxy_file = open(os.getenv("PROXYFILE") or "./proxies.txt")

    proxies =  [line for line in proxy_file.readlines()]

    print("Found %d proxies" % len(proxies))

    return proxies
