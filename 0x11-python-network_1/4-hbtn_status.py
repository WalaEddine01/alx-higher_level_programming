#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
