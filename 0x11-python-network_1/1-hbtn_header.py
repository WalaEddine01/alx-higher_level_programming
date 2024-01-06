#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""
from urllib import request
import urllib
from sys import argv

url = argv[1]
req = request.Request(url)
with request.urlopen(req) as request_:
    x_request_id = request_.getheader('X-Request-Id')
    print(f"{x_request_id}")
