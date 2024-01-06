#!/usr/bin/python3
"""
displays the value of the X-Request-Id.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with requests.get(url) as request_:
        print(request_.headers.get("X-Request-Id"))
