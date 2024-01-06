#!/usr/bin/python3
"""
displays the value of the X-Request-Id.
"""
import urllib.request
from sys import argv

url = argv[1]
with urllib.request.urlopen(url) as request_:
    x_request_id = request_.getheader('X-Request-Id')
    print(f"{x_request_id}")
