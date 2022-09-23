#!/usr/bin/python3
""" fetches status from a url"""

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as file:
    status = file.read()
print("Body response:")
print(f"\t- type: {type(status)}")
print(f"\t- content: {status}")
print(f"\t- utf8 content: {status.decode()}")
