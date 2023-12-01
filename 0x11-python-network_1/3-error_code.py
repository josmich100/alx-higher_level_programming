# !/usr/bin/python3
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    # displays body of response and manages error code
    URL = sys.argv[1]
    req = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(req) as request:
            page = request.read()
        print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
