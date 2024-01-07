#!/usr/bin/python3
"""
Python script that list 10 commits
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    req = requests.get(url)
    commits = req.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
