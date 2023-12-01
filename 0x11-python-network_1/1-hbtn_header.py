# !/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
    # fetches a URL and displays X-Request-Id variable
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        header = response.getheader('X-Request-Id')
    print(header)
