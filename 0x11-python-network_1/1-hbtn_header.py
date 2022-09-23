#!/usr/bin/python3
""" takes a URL and sends a request to the URL
    displays X-Request-Id variable if found in the header"""

from urllib.request import urlopen, Request
import sys


if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as res:
        print(res.getheader('X-Request-Id'))
