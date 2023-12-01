# !/usr/bin/python3
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # sends EMAIL POST request
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    values = {'EMAIL': EMAIL}
    DATA = urllib.parse.urlencode(values)
    DATA = DATA.encode('ascii')
    req = urllib.request.Request(URL, DATA)
    with urllib.request.urlopen(req) as request:
        html = request.read()
    print(html.decode('utf-8'))
