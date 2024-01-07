#!/usr/bin/python3
"""
Python script that list 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(e)
    try:
        commits = req.json()
    except ValueError:
        print("Not a valid JSON")
    for j in range(10):
        print("{}: {}".format(
            commits[j].get('sha'),
            commits[j].get('commit').get('author').get('name')))
