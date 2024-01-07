#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display id
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
