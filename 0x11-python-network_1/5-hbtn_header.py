#!/usr/bin/python3
""" gets header of a URL using the requests package"""


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
