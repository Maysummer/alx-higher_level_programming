#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with
the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) != 2:
        letter = ""
    else:
        letter = sys.argv[1]
    obj = {'q': letter}
    r = requests.post(url, data=obj)
    try:
        json = r.json()
        if json != {}:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except ValueError:
         print('Not a valid JSON')
