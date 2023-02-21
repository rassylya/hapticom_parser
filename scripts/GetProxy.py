import requests
from itertools import cycle
import traceback
from ProxyParser import proxyParser
from requests.exceptions import ConnectionError

def getProxy(url):
    proxies = proxyParser()
    proxy_pool = cycle(proxies)

    # Initialize a URL.

    for i in range(1,11):

    # Get a proxy from the pool

        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            print(f"Checking for proxy {proxy}, timeout:30 seconds")
            response = requests.get(url,proxies={"http": proxy, "https": proxy}, timeout=30)
            print(f"Success")
            return proxy
        except ConnectionError as e:    
            print(e)
            print("Skipping. Connection error")

