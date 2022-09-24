#!/usr/bin/python3
"""Python script that takes in a URL
   sends a request to the URL
   displays the body of the response (decoded in utf-8)"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as res:
            response = res.read()
            print(response.decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
