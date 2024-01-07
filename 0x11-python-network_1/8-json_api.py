#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    try:
        req = requests.post(url, data={'q': argv[1]})
    except IndexError:
        req = requests.post(url, data={'q': ''})
    data = req.json()
    if not data:
        print("No result")
    elif 'id' in data and 'name' in data:
        print(f"[{data['id']}] {data['name']}")
    else:
        print('Not a valid JSON')
