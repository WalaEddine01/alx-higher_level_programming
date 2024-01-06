#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as request_:
    x_request_id = request_.getheader('X-Request-Id')
    print(f"{x_request_id}")
