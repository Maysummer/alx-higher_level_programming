#!/usr/bin/python3
"""list 10 commits"""


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    r = requests.get(url)
    r = r.json()
    for commit in r[:10]:
        name = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(commit.get('sha'), name))
