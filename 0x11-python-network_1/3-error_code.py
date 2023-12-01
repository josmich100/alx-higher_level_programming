#!/usr/bin/python3
"""
Sends a request to a URL, displays the body of the response, and handles HTTP errors.
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            with request.urlopen(url) as response:
                body = response.read().decode('utf-8')
                print(body)

        except error.HTTPError as e:
            print(f"Error code: {e.code}")
    else:
        print("Usage: ./3-error_code.py <URL>")
