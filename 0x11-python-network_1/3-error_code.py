#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(page.decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
