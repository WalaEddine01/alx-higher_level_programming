#!/usr/bin/python3
"""
Python script that list 10 commits
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(e)
    try:
        commits = req.json()
    except ValueError:
        print("Not a valid JSON")
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
