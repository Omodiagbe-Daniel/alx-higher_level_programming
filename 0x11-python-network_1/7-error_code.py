#!/usr/bin/python3
"""
    Python script that takes in a URL
    sends a request to the URL
     displays the body of the response
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    if (r.status_code >= 400):
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
