#!/usr/bin/python3
"""
Python script that list 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    req = requests.get(url)
    commits = req.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get('sha'),
                commits[j].get('commit').get('author').get('name')))
    except IndexError:
        pass
