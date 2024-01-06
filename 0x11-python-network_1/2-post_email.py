#!/usr/bin/python3
"""
script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    var = argv[2]
    values = {
        'email': var
    }
    data = parse.urlencode(values)
    data = data.encode()
    req = request.Request(url, data)
    with request.urlopen(req) as request_:
        request_ = request_.read()
        print(request_.decode('utf-8'))
