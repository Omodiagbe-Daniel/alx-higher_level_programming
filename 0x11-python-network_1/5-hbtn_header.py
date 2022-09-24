#!/usr/bin/python3
""" fetches a URL using the requests package"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
