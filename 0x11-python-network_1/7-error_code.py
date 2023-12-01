#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        response = requests.get(url)
        status_code = response.status_code

        if status_code >= 400:
            print(f"Error code: {status_code}")
        else:
            print(response.text)
    else:
        print("Usage: ./7-error_code.py <URL>")
