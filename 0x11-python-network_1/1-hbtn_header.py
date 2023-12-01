#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable in the header of the response.
"""

from urllib import request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        with request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
    else:
        print("Usage: ./1-hbtn_header.py <URL>")
