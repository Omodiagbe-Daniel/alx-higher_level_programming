#!/usr/bin/python3
""" fetches a URL using the requests package"""

import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io')
    print(r.headers['X-Request-Id'])
