#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as request_:
            print(request_.read().decode('utf-8'))
    except Exception as e:
        print(f"Error code: {e.code}")
