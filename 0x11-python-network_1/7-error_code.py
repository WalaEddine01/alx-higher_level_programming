#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
