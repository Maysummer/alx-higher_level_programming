#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    usrName = sys.argv[1]
    pwd = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(usrName, pwd))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
