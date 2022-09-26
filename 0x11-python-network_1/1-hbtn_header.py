#!/usr/bin/python3
"""script that takes a url, sends a request & displays the
value of 'X-Request-ID' in the header"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
