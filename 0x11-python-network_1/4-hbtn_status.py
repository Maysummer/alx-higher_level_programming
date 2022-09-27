#!/usr/bin/python3
"""script to fetch a url, using 'requests package'"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    r = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r))
