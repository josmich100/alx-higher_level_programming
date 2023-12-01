#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the body of the response.
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        # Prepare data to be sent in the POST request
        data = parse.urlencode({'email': email}).encode('utf-8')

        # Create a POST request
        req = request.Request(url, data=data, method='POST')

        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
