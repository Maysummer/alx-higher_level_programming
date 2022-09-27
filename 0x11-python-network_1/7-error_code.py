#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the body of the response"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    err_code = r.status_code
    if err_code >= 400:
        print('Error code: {}'.format(err_code))
    else:
        print(r.text)
