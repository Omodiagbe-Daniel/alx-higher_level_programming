#!/usr/bin/python3
""" Python script that takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
    displays the body of the response (decoded in utf-8)"""

from urllib.request import Request, urlopen
import urllib.parse as parse
import sys


if __name__ == "__main___":
    data = parse.urlencode(sys.argv[2]).encode()
    req = Request(sys.argv[1], data)
    with urlopen(req) as res:
        response = res.read()
    print(response.decode('utf-8'))
