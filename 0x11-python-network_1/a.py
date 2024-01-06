#!/usr/bin/python3
import urllib.request
import urllib.parse

try:
    url = urllib.request.urlopen('http://www.google.com/search?q=test')
    print(url.read())
except Exception as e:
    print(str(e))
print("--------------------")
try:
    url2 = 'http://www.google.com/search?q=test'
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = urllib.request.Request(url2, headers=headers)
    with urllib.request.urlopen(req) as response:
        respData = response.read().decode('utf-8')

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))